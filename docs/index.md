# IChingPy

[![pypi](https://img.shields.io/badge/pypi-v0.1-blue)](https://pypi.org/project/ichingpy/)
[![codecov](https://codecov.io/gh/JinyangWang27/ichingpy/branch/main/graph/badge.svg?token=T27TSAL7BC)](https://codecov.io/gh/JinyangWang27/ichingpy)
[![license](https://img.shields.io/badge/license-MIT-g)]([LICENSE](https://github.com/JinyangWang27/ichingpy/blob/main/LICENSE))

An object-oriented Python library for working with the **I-Ching** ☯️ with type annotations.

## Motivation and Goal

Most applications (mostly divination methods) of the I-Ching are considered as superstitious. 
In Chinese, "superstitious" is defined as: to believe blindly.
This library demonstrates applications often regarded as superstitious, leaving it up to you to decide whether to believe in them or not.

These application involves complicated logics, this library implement in such a way that a proficient Python developer can easily understand how to perform those divination by just reading the code.

[Installing Ichingpy](install.md) is as simple as: `pip install ichingpy`

- Multiple languages support: both Chinese and English can be used as the display language.



## IChingPy examples

Too see IChingPy at work, let's start with a simple example, creating a hexagram from datetime now.

```python
from datetime import datetime

import ichingpy as icp

hexagram = icp.Hexagram.from_datetime(datetime.now())
hexagram
"""
-- --
-- -- X -> -----
-----
-----
-----
-----
"""
```

Create a Kou Hexagram (Coming to meet, 天风姤)
```python
gou = icp.Hexagram.from_binary([2, 1, 1, 1, 1, 1]) 
```

Create a assigner (创建一个干支装卦器)
```python
assigner = icp.SixLinesDivinationEngine()
assigner.execute(gou) 
gou

"""
壬 戌土 -----
壬 申金 -----
壬 午火 -----
辛 酉金 -----
辛 亥水 -----
辛 丑土 -- --
"""
```
Switch display language to English
```python
icp.set_language("en")
gou
"""
Geng (7) Xu   (11) EARTH -- --
Geng (7) Shen (9 ) METAL -- -- X -> -----
Geng (7) Wu   (7 ) FIRE  -----
Jia  (1) Chen (5 ) EARTH -----
Jia  (1) Yin  (3 ) WOOD  -----
Jia  (1) Zi   (1 ) WATER -----
"""
```
Background knowledge: How to pair [Heaven Stems](https://en.wikipedia.org/wiki/Heavenly_Stems) and [Earthly Branches](https://en.wikipedia.org/wiki/Earthly_Branches) to [Sexagenary Cycle](https://en.wikipedia.org/wiki/Sexagenary_cycle)?