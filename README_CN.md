
# 易经Python库

[![pypi](https://img.shields.io/badge/pypi-v0.1-blue)](https://pypi.org/project/ichingpy/)
[![codecov](https://codecov.io/gh/JinyangWang27/ichingpy/branch/main/graph/badge.svg?token=T27TSAL7BC)](https://codecov.io/gh/JinyangWang27/ichingpy)
[![license](https://img.shields.io/badge/license-MIT-g)]([LICENSE](https://github.com/JinyangWang27/ichingpy/blob/main/LICENSE))

[English README](https://github.com/JinyangWang27/ichingpy/blob/main/README.md)

```
不了解却选择盲目相信，那就是迷信。
```



## 简介
使用Python类型提示所构建的易经概念。基于规律的代码实现，无需硬编码映射。用纯Python定义哲学概念。

中华传统文化输出，目前代码主要由英语实现，后续将推出汉语版本。

作者认为周易希望人们法天效地，根据自然规律来指导为人处事。因此更应注重对卦象的理解，占卜仅供娱乐。
如有需求，在本库完成之前，作者提供解卦服务（六爻）。

### 特点

1. 支持多种方法生成卦象（蓍草，铜钱，八字）
2. 由同余类实现的天干地支算术运算
3. 解释卦象含义（TODO）
4. 根据易经进行占卜（增删卜易 TODO）

## 安装

> pip install ichingpy


## 帮助
见[文档](https://jinyangwang27.github.io/ichingpy/)获取更多细节。

## 简例

导入库，默认显示语言为汉语。

```python
import ichingpy as icp
```

如遇命令行界面汉字显示问题，使用[chcp](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chcp)命令
> chcp 936

切换显示语言至汉语。

### 公历（格里历）转八字


```python
from datetime import datetime
ba_zi = icp.FourPillars.from_datetime(datetime(2000, 7, 15, 11, 0, 0))
ba_zi.get_pillars()
#> 庚辰年 癸未月 甲戌日 庚午时
```

一个四柱 (FourPillars) 对象也有自己的字符串表示形式
```python
ba_zi
#> 庚辰 癸未 甲戌 庚午
```
干支记月的每月第一天（每个月上半月的节气），附近的转换可能不准：准确的转换需要计算黄道面中日地相对位置。
[香港天文台](https://www.hko.gov.hk/sc/gts/astronomy/Solar_Term.htm)是唯一提供公开准确的节气日期的网站。

例如，2025年立春提前一天，在2月3日，而不是平时的2月4日，
```python
icp.FourPillars.from_datetime(datetime(2025, 2,3, 11, 0, 0))
#> 甲辰 丁丑 癸卯 戊午
```
此时，可以使用以下参数来调整年月干支
```python
icp.FourPillars.from_datetime(datetime(2025, 2,3, 11, 0, 0), month_adjust=1)   
#> 乙巳 戊寅 癸卯 戊午
```
若立春在2月5日，则 month_adjust=-1


### 起卦
#### 八字起卦
给定年月日时起卦
```python
from datetime import datetime
icp.Hexagram.from_datetime(datetime(2022, 3, 31, 11, 0, 0)) 
#> 蒙 -> 未济
#> 亨。匪我求童蒙，童蒙求我。初筮告，再三渎，渎则不告。利贞。
#> 山下出泉，蒙；君子以果行育德。
#> -----
#> -- --
#> -- -- X -> -----
#> -- --
#> -----
#> -- --
#> 六四 困蒙，吝。
```
使用当前八字起卦

```python
icp.Hexagram.from_datetime(datetime.now()) 
#> 睽 -> 噬嗑
#> 小事吉。
#> 上火下泽，睽；君子以同而异。
#> -----
#> -- --
#> -----
#> -- --
#> ----- O -> -- --
#> -----
#> 九二 遇主于巷，无咎。
```

#### 铜钱起卦

```python
icp.Hexagram.from_three_coins()           
```

#### 蓍草起卦

```python
icp.Hexagram.from_yarrow_stalks()
```

### 装卦，纳干支
创建一个天风姤卦，无动爻
```python
gou = icp.Hexagram.from_binary([2, 1, 1, 1, 1, 1]) 
gou
#> 姤
#> 女壮，勿用取女。
#> 天下有风，姤；后以施命诰四方。
#> -----
#> -----
#> -----
#> -----
#> -----
#> -- --
```

创建一个干支装卦器，装卦
```python
engine = icp.SixLinesDivinationEngine()
engine.execute(gou)  
#> gou
#> 父母 壬 戌土 -----
#> 兄弟 壬 申金 -----
#> 官鬼 壬 午火 ----- 应 
#> 兄弟 辛 酉金 -----
#> 子孙 辛 亥水 -----
#> 父母 辛 丑土 -- -- 世 
```


### 干支算术运算

干支各自支持算术运算，分别为模10以及模12的同余类 $\mathbb{Z}_{10}$ 与 $\mathbb{Z}_{12}$。需注意，严格来说干支都不具备群的代数结构，因为不满足单位元(identity element)条件。

创建一个天干甲
```python
icp.HeavenlyStem.Jia + 1
#> <HeavenlyStem.Yi: 2>
```

天干甲加天干癸
```python
gui = icp.HeavenlyStem.Gui
jia = icp.HeavenlyStem.Jia
jia + gui 
#> <HeavenlyStem.Jia: 1>
```

干支组的算术运算
```python
jia = icp.HeavenlyStem.Jia 
zi = icp.EarthlyBranch.Zi
jia_zi = icp.SexagenaryCycle(jia, zi)
jia_zi
#> 甲子
jia_zi+1
#> 乙丑
jia_zi+60
#> 甲子
```
