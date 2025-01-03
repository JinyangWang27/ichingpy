# I-Ching Python

## Description
I-Ching Python is a fully object-oriented Python library for working with the I-Ching, an ancient Chinese divination text. 
This library provides tools for 
1. generating hexagrams using multiple methods, 
2. interpreting their meanings   (TODO)
3. performing divination based on the I-Ching (TODO)
4. arithmetic operations on Heavenly Stems and Earthly Branches (干支)


## Installation

> pip install ichingpy

## Quick Start


```python
import ichingpy as icp
```

Create a Line  (爻)
```python
yin = icp.Line(status=icp.LineStatus.CHANGING)
```

Create a Trigram (八卦)
```python
qian = icp.Trigram.from_binary([1, 1, 1])
```


Create a Hexagram with transformation (变卦)
```python
qian_tai = icp.Hexagram.from_binary([3, 3, 3, 1, 1, 1]) # 乾之泰
```

A Hexagram can be also generated by using 50 yarrow stalks or 3 coins
```python 
hexagram = icp.Hexagram.from_three_coins()

```
```python 
hexagram = icp.Hexagram.from_yarrow_stalks()
```

```
-- --
-- --
-- --
----- O -> -- --
-- --
----- O -> -- --
```

Assign HeavenlyStems to a hexagram
```python
from ichingpy.calculator.assigner import HexagramAssigner
hexagram = icp.Hexagram.from_yarrow_stalks()
assigner = HexagramAssigner()
assigner.assign_stems(hexagram)
hexagram.inner.stem
```
```
[<HeavenlyStem.Ji: 6>, <HeavenlyStem.Ji: 6>, <HeavenlyStem.Ji: 6>]
```

#### Arithmetic operations on Heavenly Stems and Earthly Branches (干支)

```python
>>> icp.HeavenlyStem.Jia + 1
<HeavenlyStem.Yi: 2>

>>> gui = icp.HeavenlyStem.Gui
>>> jia = icp.HeavenlyStem.Jia
>>> jia + gui 
<HeavenlyStem.Jia: 1>
```
```python
>>> jia = icp.HeavenlyStem.Jia 
>>> zi = icp.EarthlyBranch.Zi
>>> jia_zi = icp.SexagenaryCycle(jia, zi)
>>> jia_zi
甲子
>>> jia_zi+1
乙丑
>>> jia_zi+60
甲子
```