# Convolutional neural networks for computer vision

[![Build Status](https://travis-ci.org/osmr/imgclsmob.svg?branch=master)](https://travis-ci.org/osmr/imgclsmob)
[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-2.7%2C3.6%2C3.7-lightgrey.svg)](https://github.com/osmr/imgclsmob)

This repo is used to research convolutional networks for task of computer vision. For this purpose, the repo contains
(re)implementations of various classification and segmentation models and scripts for training/evaluating/converting.

The following frameworks are used:
- MXNet/Gluon ([info](https://mxnet.apache.org)),
- PyTorch ([info](https://pytorch.org)),
- Chainer ([info](https://chainer.org)),
- Keras ([info](https://keras.io)),
- TensorFlow ([info](https://www.tensorflow.org)).

For each supported framework, there is a PIP-package containing pure models without auxiliary scripts. List of packages:
- [gluoncv2](https://pypi.org/project/gluoncv2) for Gluon,
- [pytorchcv](https://pypi.org/project/pytorchcv) for PyTorch,
- [chainercv2](https://pypi.org/project/chainercv2) for Chainer,
- [kerascv](https://pypi.org/project/kerascv) for Keras,
- [tensorflowcv](https://pypi.org/project/tensorflowcv) for TensorFlow.

Currently, models are mostly implemented on Gluon and then ported to other frameworks. Some models are pretrained on
[ImageNet-1K](http://www.image-net.org), [CIFAR-10/100](https://www.cs.toronto.edu/~kriz/cifar.html),
[SVHN](http://ufldl.stanford.edu/housenumbers), [CUB-200-2011](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html),
[Pascal VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012), [ADE20K](http://groups.csail.mit.edu/vision/datasets/ADE20K),
[Cityscapes](https://www.cityscapes-dataset.com), and [COCO](http://cocodataset.org) datasets. All pretrained weights
are loaded automatically during use. See examples of such automatic loading of weights in the corresponding sections of
the documentation dedicated to a particular package:
- [Gluon models](gluon/README.md),
- [PyTorch models](pytorch/README.md),
- [Chainer models](chainer_/README.md),
- [Keras models](keras_/README.md),
- [TensorFlow models](tensorflow_/README.md).

## Installation

To use training/evaluating scripts as well as all models, you need to clone the repository and install dependencies:
```
git clone git@github.com:osmr/imgclsmob.git
pip install -r requirements.txt
```

## Table of implemented classification models

Some remarks:
- `Repo` is an author repository, if it exists.
- `A`, `B`, `C`, `D`, and `E` means the implementation of a model for ImageNet-1K, CIFAR-10, CIFAR-100, SVHN, and CUB-200-2011, respectively.
- `A+`, `B+`, `C+`, `D+`, and `E+` means having a pre-trained model for corresponding datasets.

| Model | [Gluon](gluon/README.md) | [PyTorch](pytorch/README.md) | [Chainer](chainer_/README.md) | [Keras](keras_/README.md) | [TF](tensorflow_/README.md) | Paper | Repo | Year |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AlexNet | A+ | A+ | A+ | A+ | A+ | [link](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) | [link](https://code.google.com/archive/p/cuda-convnet2) | 2012 |
| ZFNet | A | A | A | - | - | [link](https://arxiv.org/abs/1311.2901) | - | 2013 |
| VGG | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1409.1556) | - | 2014 |
| BN-VGG | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1409.1556) | - | 2015 |
| BN-Inception | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1502.03167) | - | 2015 |
| ResNet | A+B+C+D+E+ | A+B+C+D+E+ | A+B+C+D+E+ | A+ | A+ | [link](https://arxiv.org/abs/1512.03385) | [link](https://github.com/KaimingHe/deep-residual-networks) | 2015 |
| PreResNet | A+B+C+D+ | A+B+C+D+ | A+B+C+D+ | A+ | A+ | [link](https://arxiv.org/abs/1603.05027) | [link](https://github.com/facebook/fb.resnet.torch) | 2016 |
| ResNeXt | A+B+C+D+ | A+B+C+D+ | A+B+C+D+ | A+ | A+ | [link](http://arxiv.org/abs/1611.05431) | [link](https://github.com/facebookresearch/ResNeXt) | 2016 |
| SENet | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1709.01507) | [link](https://github.com/hujie-frank/SENet) | 2017 |
| SE-ResNet | A+B+C+D+E+ | A+B+C+D+E+ | A+B+C+D+E+ | A+ | A+ | [link](https://arxiv.org/abs/1709.01507) | [link](https://github.com/hujie-frank/SENet) | 2017 |
| SE-PreResNet | A | A | A | A | A | [link](https://arxiv.org/abs/1709.01507) | [link](https://github.com/hujie-frank/SENet) | 2017 |
| SE-ResNeXt | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1709.01507) | [link](https://github.com/hujie-frank/SENet) | 2017 |
| IBN-ResNet | A+ | A+ | - | - | - | [link](https://arxiv.org/abs/1807.09441) | [link](https://github.com/XingangPan/IBN-Net) | 2018 |
| IBN-ResNeXt | A+ | A+ | - | - | - | [link](https://arxiv.org/abs/1807.09441) | [link](https://github.com/XingangPan/IBN-Net) | 2018 |
| IBN-DenseNet | A+ | A+ | - | - | - | [link](https://arxiv.org/abs/1807.09441) | [link](https://github.com/XingangPan/IBN-Net) | 2018 |
| AirNet | A+ | A+ | A+ | - | - | [link](https://ieeexplore.ieee.org/document/8510896) | [link](https://github.com/soeaver/AirNet-PyTorch) | 2018 |
| AirNeXt | A+ | A+ | A+ | - | - | [link](https://ieeexplore.ieee.org/document/8510896) | [link](https://github.com/soeaver/AirNet-PyTorch) | 2018 |
| BAM-ResNet | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1807.06514) | [link](https://github.com/Jongchan/attention-module) | 2018 |
| CBAM-ResNet | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1807.06521) | [link](https://github.com/Jongchan/attention-module) | 2018 |
| ResAttNet | A | A | A | - | - | [link](https://arxiv.org/abs/1704.06904) | [link](https://github.com/fwang91/residual-attention-network) | 2017 |
| SKNet | A | A | A | - | - | [link](https://arxiv.org/abs/1903.06586) | [link](https://github.com/implus/SKNet) | 2019 |
| DIA-ResNet | AB+C+D+ | AB+C+D+ | AB+C+D+ | - | - | [link](https://arxiv.org/abs/1905.10671) | [link](https://github.com/gbup-group/DIANet) | 2019 |
| DIA-PreResNet | AB+C+D+ | AB+C+D+ | AB+C+D+ | - | - | [link](https://arxiv.org/abs/1905.10671) | [link](https://github.com/gbup-group/DIANet) | 2019 |
| PyramidNet | A+B+C+D+ | A+B+C+D+ | A+B+C+D+ | - | - | [link](https://arxiv.org/abs/1610.02915) | [link](https://github.com/jhkim89/PyramidNet) | 2016 |
| DiracNetV2 | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1706.00388) | [link](https://github.com/szagoruyko/diracnets) | 2017 |
| ShaResNet | A | A | A | - | - | [link](https://arxiv.org/abs/1702.08782) | [link](https://github.com/aboulch/sharesnet) | 2017 |
| CRU-Net | A+ | - | - | - | - | [link](https://www.ijcai.org/proceedings/2018/88) | [link](https://github.com/cypw/CRU-Net) | 2018 |
| DenseNet | A+B+C+D+ | A+B+C+D+ | A+B+C+D+ | A+ | A+ | [link](https://arxiv.org/abs/1608.06993) | [link](https://github.com/liuzhuang13/DenseNet) | 2016 |
| CondenseNet | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1711.09224) | [link](https://github.com/ShichenLiu/CondenseNet) | 2017 |
| SparseNet | A | A | A | - | - | [link](https://arxiv.org/abs/1801.05895) | [link](https://github.com/Lyken17/SparseNet) | 2018 |
| PeleeNet | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1804.06882) | [link](https://github.com/Robert-JunWang/Pelee) | 2018 |
| Oct-ResNet | ABCD | A | A | - | - | [link](https://arxiv.org/abs/1904.05049) | - | 2019 |
| Res2Net | A | - | - | - | - | [link](https://arxiv.org/abs/1904.01169) | - | 2019 |
| WRN | A+B+C+D+ | A+B+C+D+ | A+B+C+D+ | - | - | [link](https://arxiv.org/abs/1605.07146) | [link](https://github.com/szagoruyko/wide-residual-networks) | 2016 |
| WRN-1bit | B+C+D+ | B+C+D+ | B+C+D+ | - | - | [link](https://arxiv.org/abs/1802.08530) | [link](https://github.com/McDonnell-Lab/1-bit-per-weight) | 2018 |
| DRN-C | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1705.09914) | [link](https://github.com/fyu/drn) | 2017 |
| DRN-D | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1705.09914) | [link](https://github.com/fyu/drn) | 2017 |
| DPN | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1707.01629) | [link](https://github.com/cypw/DPNs) | 2017 |
| DarkNet Ref | A+ | A+ | A+ | A+ | A+ | [link](https://github.com/pjreddie/darknet) | [link](https://github.com/pjreddie/darknet) | - |
| DarkNet Tiny | A+ | A+ | A+ | A+ | A+ | [link](https://github.com/pjreddie/darknet) | [link](https://github.com/pjreddie/darknet) | - |
| DarkNet-19 | A | A | A | A | A | [link](https://github.com/pjreddie/darknet) | [link](https://github.com/pjreddie/darknet) | - |
| DarkNet-53 | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1804.02767) | [link](https://github.com/pjreddie/darknet) | 2018 |
| ChannelNet | A | A | A | - | A | [link](https://arxiv.org/abs/1809.01330) | [link](https://github.com/HongyangGao/ChannelNets) | 2018 |
| iSQRT-COV-ResNet | A | A | - | - | - | [link](https://arxiv.org/abs/1712.01034) | [link](https://github.com/jiangtaoxie/fast-MPN-COV) | 2017 |
| RevNet | - | A | - | - | - | [link](https://arxiv.org/abs/1707.04585) | [link](https://github.com/renmengye/revnet-public) | 2017 |
| i-RevNet | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1802.07088) | [link](https://github.com/jhjacobsen/pytorch-i-revnet) | 2018 |
| BagNet | A+ | A+ | A+ | - | - | [link](https://openreview.net/pdf?id=SkfMWhAqYQ) | [link](https://github.com/wielandbrendel/bag-of-local-features-models) | 2019 |
| DLA | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1707.06484) | [link](https://github.com/ucbdrive/dla) | 2017 |
| MSDNet | A | AB | - | - | - | [link](https://arxiv.org/abs/1703.09844) | [link](https://github.com/gaohuang/MSDNet) | 2017 |
| FishNet | A+ | A+ | A+ | - | - | [link](http://papers.nips.cc/paper/7356-fishnet-a-versatile-backbone-for-image-region-and-pixel-level-prediction.pdf) | [link](https://github.com/kevin-ssy/FishNet) | 2018 |
| ESPNetv2 | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1811.11431) | [link](https://github.com/sacmehta/ESPNetv2) | 2018 |
| X-DenseNet | AB+C+D+ | AB+C+D+ | AB+C+D+ | - | - | [link](https://arxiv.org/abs/1711.08757) | [link](https://github.com/DrImpossible/Deep-Expander-Networks) | 2017 |
| SqueezeNet | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1602.07360) | [link](https://github.com/DeepScale/SqueezeNet) | 2016 |
| SqueezeResNet | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1602.07360) | - | 2016 |
| SqueezeNext | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1803.10615) | [link](https://github.com/amirgholami/SqueezeNext) | 2018 |
| ShuffleNet | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1707.01083) | - | 2017 |
| ShuffleNetV2 | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1807.11164) | - | 2018 |
| MENet | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1803.09127) | [link](https://github.com/clavichord93/MENet) | 2018 |
| MobileNet | A+E+ | A+E+ | A+E+ | A+ | A+ | [link](https://arxiv.org/abs/1704.04861) | [link](https://github.com/tensorflow/models) | 2017 |
| FD-MobileNet | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1802.03750) | [link](https://github.com/clavichord93/FD-MobileNet) | 2018 |
| MobileNetV2 | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1801.04381) | [link](https://github.com/tensorflow/models) | 2018 |
| MobileNetV3 | A | A | A | - | - | [link](https://arxiv.org/abs/1905.02244) | - | 2019 |
| IGCV3 | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1806.00178) | [link](https://github.com/homles11/IGCV3) | 2018 |
| MnasNet | A+ | A+ | A+ | A+ | A+ | [link](https://arxiv.org/abs/1807.11626) | - | 2018 |
| DARTS | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1806.09055) | [link](https://github.com/quark0/darts) | 2018 |
| ProxylessNAS | A+E+ | A+E+ | A+E+ | - | - | [link](https://arxiv.org/abs/1812.00332) | [link](https://github.com/mit-han-lab/ProxylessNAS) | 2018 |
| Xception | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1610.02357) | [link](https://github.com/fchollet/deep-learning-models) | 2016 |
| InceptionV3 | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1512.00567) | [link](https://github.com/tensorflow/models) | 2015 |
| InceptionV4 | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1602.07261) | [link](https://github.com/tensorflow/models) | 2016 |
| InceptionResNetV2 | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1602.07261) | [link](https://github.com/tensorflow/models) | 2016 |
| PolyNet | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1611.05725) | [link](https://github.com/open-mmlab/polynet) | 2016 |
| NASNet-Large | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1707.07012) | [link](https://github.com/tensorflow/models) | 2017 |
| NASNet-Mobile | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1707.07012) | [link](https://github.com/tensorflow/models) | 2017 |
| PNASNet-Large | A+ | A+ | A+ | - | - | [link](https://arxiv.org/abs/1712.00559) | [link](https://github.com/tensorflow/models) | 2017 |
| EfficientNet | A+ | A+ | A+ | A+ | - | [link](https://arxiv.org/abs/1905.11946) | [link](https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet) | 2019 |
| NIN | B+C+D+ | B+C+D+ | B+C+D+ | - | - | [link](https://arxiv.org/abs/1312.4400) | [link](https://gist.github.com/mavenlin/e56253735ef32c3c296d) | 2013 |
| RoR-3 | B+C+D+ | B+C+D+ | B+C+D+ | - | - | [link](https://arxiv.org/abs/1608.02908) | - | 2016 |
| RiR | B+C+D+ | B+C+D+ | B+C+D+ | - | - | [link](https://arxiv.org/abs/1603.08029) | - | 2016 |
| ResDrop-ResNet | BCD | BCD | BCD | - | - | [link](https://arxiv.org/abs/1603.09382) | [link](https://github.com/yueatsprograms/Stochastic_Depth) | 2016 |
| Shake-Shake-ResNet | B+C+D+ | B+C+D+ | B+C+D+ | - | - | [link](https://arxiv.org/abs/1705.07485) | [link](https://github.com/xgastaldi/shake-shake) | 2017 |
| ShakeDrop-ResNet | BCD | BCD | BCD | - | - | [link](https://arxiv.org/abs/1802.02375) | - | 2018 |
| FractalNet | BC | BC | - | - | - | [link](https://arxiv.org/abs/1605.07648) | [link](https://github.com/gustavla/fractalnet) | 2016 |
| NTS-Net | E+ | E+ | E+ | - | - | [link](https://arxiv.org/abs/1809.00287) | [link](https://github.com/yangze0930/NTS-Net) | 2018 |

## Table of implemented segmentation models

Some remarks:
- `A` corresponds to Pascal VOC2012.
- `B` corresponds to Pascal ADE20K.
- `C` corresponds to Pascal Cityscapes.
- `D` corresponds to Pascal COCO.

| Model | [Gluon](gluon/README.md) | [PyTorch](pytorch/README.md) | [Chainer](chainer_/README.md) | [Keras](keras_/README.md) | [TensorFlow](tensorflow_/README.md) | Paper | Repo | Year |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PSPNet | A+B+C+D+ | A+B+C+D+ | A+B+C+D+ | - | - | [link](https://arxiv.org/abs/1612.01105) | - | 2016 |
| DeepLabv3 | A+B+CD+ | A+B+CD+ | A+B+CD+ | - | - | [link](https://arxiv.org/abs/1706.05587) | - | 2017 |
| FCN-8s(d) | A+B+CD+ | A+B+CD+ | A+B+CD+ | - | - | [link](https://arxiv.org/abs/1411.4038) | - | 2014 |
