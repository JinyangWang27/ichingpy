# Hexagram generation (起卦)

IChingPy Supports different classical methods for generating a hexagram.

## From 50 yarrow stalks (蓍草起卦)

```python
import ichingpy as icp
hexagram = icp.Hexagram.from_yarrow_stalks()
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

## From 3 coins (铜钱起卦)
```python
hexagram = icp.Hexagram.from_three_coins()
```

## From datetime
IChingPy will first convert a datetime object into [FourPillars](api/model/four_pillars.md)(八字/四柱), and generate a hexagram using the FourPillars.
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

See [LineStatus](api/enum/line_status.md) for explanation of the numbers.