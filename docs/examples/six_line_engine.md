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