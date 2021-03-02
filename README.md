# TextRecognitionDataGenerator [![TravisCI](https://travis-ci.org/Belval/TextRecognitionDataGenerator.svg?branch=master)](https://travis-ci.org/Belval/TextRecognitionDataGenerator) [![PyPI version](https://badge.fury.io/py/trdg.svg)](https://badge.fury.io/py/trdg) [![codecov](https://codecov.io/gh/Belval/TextRecognitionDataGenerator/branch/master/graph/badge.svg)](https://codecov.io/gh/Belval/TextRecognitionDataGenerator) [![Documentation Status](https://readthedocs.org/projects/textrecognitiondatagenerator/badge/?version=latest)](https://textrecognitiondatagenerator.readthedocs.io/en/latest/?badge=latest) [![mattermost](https://img.shields.io/badge/help-mattermost-blue)](https://mattermost.belval.org/signup_user_complete/?id=6j1pj6itd7y4781o1u813796ry)

## 介绍

一个生成crnn训练数据集的工具，主要针对数字、简体中文。(crnn模型训练可参考此项目[crnn](https://github.com/lvjianjin/crnn))

## 示例
### 数字
![number](./image/number.png "数字")
### 简体中文
![chinese](./image/chinese.png "中文")
## 特性

1. 本项目主要继承至[TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator) 。
2. 针对简体中文、中文数据集生成。
3. 支持自定义字体.
4. 支持自定义背景.
5. 支持自定义语料.

## 必要条件

- Python 3.6+

## 近期更新

**`2021-3-1`**: 初版上线，支持数字生成。
**`2021-3-2`**: 支持简体中文生成及自定义语料。

## 内容

- [安装](#安装)
- [使用](#使用)
    - [准备](#准备)
    - [生成](#生成)
    
## 安装

安装所需python包
```
pip install -r requirements.txt
```

## 使用
下面我们以如何创建一个数字数据集为例。
### 准备

1. 字体文件

将所准备的所有字体文件放置在./trdg/fonts/num/中。

2. 背景图片

将所准备的所有背景图片放置在./trdg/images/中。

3. 自定义语料(可选，中文必选)

准备形如./trdg/dicts/text.txt文件，并替换改文件。

### 生成

修改./trdg/main.py中的path路径后，执行main.py文件即可生成图片。
生成的图片位于./trdg/output/data/文件夹中。

## 联系

1. 邮箱：jianjinlv@163.com
2. QQ群：1081332609
