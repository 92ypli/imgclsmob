"""
    ZFNet for ImageNet-1K, implemented in Chainer.
    Original paper: 'Visualizing and Understanding Convolutional Networks,' https://arxiv.org/abs/1311.2901.
"""

__all__ = ['ZFNet', 'zfnet']

import os
import chainer.functions as F
import chainer.links as L
from chainer import Chain
from functools import partial
from chainer.serializers import load_npz
from .common import SimpleSequential


class ZFNetConv(Chain):
    """
    ZFNet specific convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    ksize : int or tuple/list of 2 int
        Convolution window size.
    stride : int or tuple/list of 2 int
        Stride of the convolution.
    pad : int or tuple/list of 2 int
        Padding value for convolution layer.
    """

    def __init__(self,
                 in_channels,
                 out_channels,
                 ksize,
                 stride,
                 pad):
        super(ZFNetConv, self).__init__()
        with self.init_scope():
            self.conv = L.Convolution2D(
                in_channels=in_channels,
                out_channels=out_channels,
                ksize=ksize,
                stride=stride,
                pad=pad,
                nobias=False)
            self.activ = F.relu

    def __call__(self, x):
        x = self.conv(x)
        x = self.activ(x)
        return x


class ZFNetReduceBlock(Chain):
    """
    ZFNet reduce block.

    Parameters:
    ----------
    nsize : int, default 5
        Amount of neighbouring channels used for normalization.
    """
    def __init__(self,
                 nsize=5):
        super(ZFNetReduceBlock, self).__init__()
        self.nsize = nsize

        with self.init_scope():
            self.pool = partial(
                F.max_pooling_2d,
                ksize=3,
                stride=2,
                pad=1,
                cover_all=False)
            self.norm = partial(
                F.local_response_normalization,
                n=nsize,
                k=2.0)

    def __call__(self, x):
        x = self.pool(x)
        x = self.norm(x)
        return x


class ZFNetDense(Chain):
    """
    ZFNet specific dense block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    """

    def __init__(self,
                 in_channels,
                 out_channels):
        super(ZFNetDense, self).__init__()
        with self.init_scope():
            self.fc = L.Linear(
                in_size=in_channels,
                out_size=out_channels)
            self.activ = F.relu
            self.dropout = partial(
                F.dropout,
                ratio=0.5)

    def __call__(self, x):
        x = self.fc(x)
        x = self.activ(x)
        x = self.dropout(x)
        return x


class ZFNetOutputBlock(Chain):
    """
    ZFNet specific output block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    classes : int
        Number of classification classes.
    """
    def __init__(self,
                 in_channels,
                 classes):
        super(ZFNetOutputBlock, self).__init__()
        mid_channels = 4096

        with self.init_scope():
            self.fc1 = ZFNetDense(
                in_channels=in_channels,
                out_channels=mid_channels)
            self.fc2 = ZFNetDense(
                in_channels=mid_channels,
                out_channels=mid_channels)
            self.fc3 = L.Linear(
                in_size=mid_channels,
                out_size=classes)

    def __call__(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


class ZFNet(Chain):
    """
    AlexNet model from 'One weird trick for parallelizing convolutional neural networks,'
    https://arxiv.org/abs/1404.5997.

    Parameters:
    ----------
    channels : list of list of int
        Number of output channels for each unit.
    ksizes : list of list of int
        Convolution window sizes for each unit.
    strides : list of list of int or tuple/list of 2 int
        Strides of the convolution for each unit.
    pads : list of list of int or tuple/list of 2 int
        Padding value for convolution layer for each unit.
    in_channels : int, default 3
        Number of input channels.
    in_size : tuple of two ints, default (224, 224)
        Spatial size of the expected input image.
    classes : int, default 1000
        Number of classification classes.
    """
    def __init__(self,
                 channels,
                 ksizes,
                 strides,
                 pads,
                 in_channels=3,
                 in_size=(224, 224),
                 classes=1000):
        super(ZFNet, self).__init__()
        self.in_size = in_size
        self.classes = classes

        with self.init_scope():
            self.features = SimpleSequential()
            with self.features.init_scope():
                for i, channels_per_stage in enumerate(channels):
                    stage = SimpleSequential()
                    with stage.init_scope():
                        if i != 0:
                            setattr(stage, "reduce{}".format(i + 1), ZFNetReduceBlock())
                        for j, out_channels in enumerate(channels_per_stage):
                            setattr(stage, "unit{}".format(j + 1), ZFNetConv(
                                in_channels=in_channels,
                                out_channels=out_channels,
                                ksize=ksizes[i][j],
                                stride=strides[i][j],
                                pad=pads[i][j]))
                            in_channels = out_channels
                    setattr(self.features, "stage{}".format(i + 1), stage)
                setattr(self.features, "final_pool", partial(
                    F.max_pooling_2d,
                    ksize=3,
                    stride=2,
                    cover_all=False))

            in_channels = in_channels * 6 * 6
            self.output = SimpleSequential()
            with self.output.init_scope():
                setattr(self.output, 'flatten', partial(
                    F.reshape,
                    shape=(-1, in_channels)))
                setattr(self.output, 'classifier', ZFNetOutputBlock(
                    in_channels=in_channels,
                    classes=classes))

    def __call__(self, x):
        x = self.features(x)
        x = self.output(x)
        return x


def get_alexnet(model_name=None,
                pretrained=False,
                root=os.path.join("~", ".chainer", "models"),
                **kwargs):
    """
    Create ZFNet model with specific parameters.

    Parameters:
    ----------
    model_name : str or None, default None
        Model name for loading pretrained model.
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    channels = [[96], [256], [384, 384, 256]]
    ksizes = [[7], [5], [3, 3, 3]]
    strides = [[2], [2], [1, 1, 1]]
    pads = [[1], [0], [1, 1, 1]]

    net = ZFNet(
        channels=channels,
        ksizes=ksizes,
        strides=strides,
        pads=pads,
        **kwargs)

    if pretrained:
        if (model_name is None) or (not model_name):
            raise ValueError("Parameter `model_name` should be properly initialized for loading pretrained model.")
        from .model_store import get_model_file
        load_npz(
            file=get_model_file(
                model_name=model_name,
                local_model_store_dir_path=root),
            obj=net)

    return net


def zfnet(**kwargs):
    """
    ZFNet model from 'Visualizing and Understanding Convolutional Networks,' https://arxiv.org/abs/1311.2901.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    return get_alexnet(model_name="zfnet", **kwargs)


def _test():
    import numpy as np
    import chainer

    chainer.global_config.train = False

    pretrained = False

    models = [
        zfnet,
    ]

    for model in models:
        net = model(pretrained=pretrained)
        weight_count = net.count_params()
        print("m={}, {}".format(model.__name__, weight_count))
        assert (model != zfnet or weight_count == 62357608)

        x = np.zeros((1, 3, 224, 224), np.float32)
        y = net(x)
        assert (y.shape == (1, 1000))


if __name__ == "__main__":
    _test()
