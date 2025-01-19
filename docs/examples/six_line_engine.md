# Six Line Divination (六爻占卜)


Create a Kou Hexagram (Coming to meet, 天风姤)
```python
import ichingpy as icp
gou = icp.Hexagram.from_binary([2, 1, 1, 1, 1, 1]) 
```

Create a assigner (创建一个干支装卦器), the default display language is Chinese.
```python
assigner = icp.SixLinesDivinationEngine()
assigner.execute(gou) 
gou

"""
父母 壬 戌土 -----
兄弟 壬 申金 -----
官鬼 壬 午火 -----
兄弟 辛 酉金 -----
子孙 辛 亥水 -----
父母 辛 丑土 -- --
"""
```
Switch display language to English
```python
icp.set_language("en")
gou
"""
PARENTS  Ren  (9) Xu   (11) EARTH -----
SIBLINGS Ren  (9) Shen (9 ) METAL -----
OFFICIALSRen  (9) Wu   (7 ) FIRE  -----
SIBLINGS Xin  (8) You  (10) METAL -----
CHILDREN Xin  (8) Hai  (12) WATER -----
PARENTS  Xin  (8) Chou (2 ) EARTH -- --
"""
```