# Hexagram generation (起卦)

IChingPy Supports different classical methods for generating a hexagram.
The default explanation/divination is provided using the text and image from I-Ching.
## From 50 yarrow stalks (蓍草起卦)
```python
import ichingpy as icp
hexagram = icp.Hexagram.from_yarrow_stalks()
hexagram
"""
萃 -> 比
亨，王假有庙，利见大人，亨，利贞，用大牲吉，利有攸往。
泽上于地，萃；君子以除戎器，戒不虞。
-- --
-----
----- O -> -- --
-- --
-- --
-- --
九四 大吉，无咎。
"""
```

The default display language is Chinese. Switch to English. 
```python
import ichingpy as icp
icp.set_language("en")
```
Text and Image translation not added yet. Six Lines divination supports English display.

## From 3 coins (铜钱起卦)
```python
hexagram = icp.Hexagram.from_three_coins()
```

## From datetime
IChingPy will first convert a datetime object into [FourPillars](../api/model/four_pillars.md)(八字/四柱), and generate a hexagram using the FourPillars.
```python
from datetime import datetime 

hexagram = icp.Hexagram.from_datetime(datetime.now())
```

Or you can use any datetime
```python
hexagram = icp.Hexagram.from_datetime(datetime(2020, 1, 1, 12, 0, 0, 0))
```


## User-defined Hexagram, from binary
You can create any Hexagram using "binary" input
```python
hexagram = icp.Hexagram.from_binary([1, 1, 1, 0, 0, 0])
```

- 0: CHANGING_YIN，unbroken line, will change (老阴/太阴)
- 1: STATIC_YANG, unbroken line  (少阳)
- 2: STATIC_YIN, broken line (少阴)
- 3: CHANGING_YANG, broken line, will change (老阳， 太阳)

See [LineStatus](../api/enum/line_status.md) for explanation of the numbers.