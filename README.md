# I-Ching Python
[![pypi](https://img.shields.io/badge/pypi-v0.1-blue)](https://pypi.org/project/ichingpy/)
[![codecov](https://codecov.io/gh/JinyangWang27/ichingpy/branch/main/graph/badge.svg?token=T27TSAL7BC)](https://codecov.io/gh/JinyangWang27/ichingpy)
[![license](https://img.shields.io/badge/license-MIT-g)]([LICENSE](https://github.com/JinyangWang27/ichingpy/blob/main/LICENSE))

[汉语文档由此](https://github.com/JinyangWang27/ichingpy/blob/main/README_CN.md)

[Foreword by Carl Gustav Jung](https://github.com/JinyangWang27/ichingpy/blob/main/docs/books/en/RichardWilhelm/foreword_CG_Jung.md)

## Description
I-Ching objects construction using Python type hints.

Pattern-based implementation without hard-coded mappings. Define how philosophical concepts in pure Python.

Features

1. Generating hexagrams using multiple methods (yarrow stalks, three coins, datetime), 
2. Arithmetic operations on Heavenly Stems and Earthly Branches (干支)
3. Multi-language support (Chinese and English)
3. Interpreting meanings of hexagrams   (TODO)
4. Performing divination based on the I-Ching (TODO)

## Installation

> pip install ichingpy

## Help

See [Documentation](https://jinyangwang27.github.io/ichingpy/) for more details.

## A Simple Example

```python
import ichingpy as icp
icp.set_language("en")
```
#### Arithmetic operations on Heavenly Stems and Earthly Branches (干支)

```python
icp.HeavenlyStem.Jia + 1
<HeavenlyStem.Yi: 2>

gui = icp.HeavenlyStem.Gui
jia = icp.HeavenlyStem.Jia
jia + gui 
#> <HeavenlyStem.Jia: 1>
```

```python
jia = icp.HeavenlyStem.Jia 
zi = icp.EarthlyBranch.Zi
jia_zi = icp.SexagenaryCycle(jia, zi)
jia_zi
#> Jia Zi
jia_zi+1
#> Yi Chou
jia_zi+60
#> Jia Zi
```
#### Assign Stem and Branch to a hexagram (装卦、纳甲)
```python
gou = icp.Hexagram.from_binary([2, 1, 1, 1, 1, 1]) 
gou
"""
-----
-----
-----
-----
-----
-- --
"""
assigner = icp.SixLinesDivinationEngine()
assigner.execute(gou) 
gou
"""
PARENTS  Ren  (9) Xu   (11) EARTH -----
SIBLINGS Ren  (9) Shen (9 ) METAL -----
OFFICIALSRen  (9) Wu   (7 ) FIRE  ----- OBJECT
SIBLINGS Xin  (8) You  (10) METAL -----
CHILDREN Xin  (8) Hai  (12) WATER -----
PARENTS  Xin  (8) Chou (2 ) EARTH -- -- SUBJECT
"""
```