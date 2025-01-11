# Datetime to FourPillars (公历时间转八字)

IChingPy enables the conversion from a datetime object (Georgian calendar) into a Four Pillar object (格里历年月日时转换成八字/四柱). 

```python
from datetime import datetime

import ichingpy as icp
ba_zi = icp.FourPillars.from_datetime(datetime(2000, 7, 15, 11, 0, 0))
ba_zi.get_pillars()
#> 庚辰年 癸未月 甲戌日 庚午时
```

A FourPillars object has its string representation
```python
ba_zi
#> 庚辰 癸未 甲戌 庚午
```

The first day of each month in the FourPillars calendar (the solar term in the first half of each month) may not be accurate: precise conversion requires calculating the relative position of the sun and the earth in the ecliptic plane. [The Hong Kong Observatory](https://www.hko.gov.hk/sc/gts/astronomy/Solar_Term.ht) is the only website that provides publicly accurate solar term dates.

For example, in 2025, the Beginning of Spring (Lichun) is one day earlier, on February 3rd, instead of the usual February 4th.

干支记月的每月第一天（每个月上半月的节气），附近的转换可能不准：准确的转换需要计算黄道面中日地相对位置。
[香港天文台](https://www.hko.gov.hk/sc/gts/astronomy/Solar_Term.htm)是唯一提供公开准确的节气日期的网站。

For example, the Beginning of Spring in 2025 is on the Feb. 3, instead of Feb. 4

例如，2025年立春提前一天，在2月3日，而不是平时的2月4日，
```python
>>> icp.FourPillars.from_datetime(datetime(2025, 2,3, 11, 0, 0))
甲辰 丁丑 癸卯 戊午
```
The parameter *month_adjust* can be used to adjust the month pillar (the year pillar will be adjusted accordingly).

此时，可以使用以下参数来调整年月干支
```python
>>> icp.FourPillars.from_datetime(datetime(2025, 2,3, 11, 0, 0), month_adjust=1)   
乙巳 戊寅 癸卯 戊午
```

If the Beginning of Spring falls on Feb. 5, then *month_adjust=-1*

若立春在2月5日，则 month_adjust=-1