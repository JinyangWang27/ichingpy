
# 易经Python库

[![pypi](https://img.shields.io/badge/pypi-v0.1-blue)](https://pypi.org/project/ichingpy/)
[![license](https://img.shields.io/badge/license-MIT-g)]([LICENSE](https://github.com/JinyangWang27/ichingpy/blob/main/LICENSE))

```
不了解却选择盲目相信，那就是迷信。
```



## 简介
使用Python类型提示所构建的易经概念。基于规律的代码实现，无需硬编码映射。用纯Python定义哲学概念。

中华传统文化输出，目前代码主要由英语实现，后续将推出汉语版本。

作者认为周易希望人们法天效地，根据自然规律来指导为人处事。因此更应注重对卦象的理解，占卜仅供娱乐。
如有需求，在本库完成之前，作者提供解卦服务（六爻）。

### 特点

1. 支持多种方法生成卦象（蓍草，铜钱，时间）
2. 由同余类实现的天干地支算术运算
3. 解释卦象含义（TODO）
4. 根据易经进行占卜（增删卜易 TODO）


## 简例

### 干支算术运算

干支各自支持算术运算，分别为模10以及模12的同余类 $\mathbb{Z}_{10}$ 与 $\mathbb{Z}_{12}$。需注意，严格来说干支都不具备群的代数结构，因为不满足单位元(identity element)条件。

创建一个天干甲
```python
>>> icp.HeavenlyStem.Jia + 1
<HeavenlyStem.Yi: 2>

天干甲加天干癸
>>> gui = icp.HeavenlyStem.Gui
>>> jia = icp.HeavenlyStem.Jia
>>> jia + gui 
<HeavenlyStem.Jia: 1>
```

干支组的数学运算
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

### 装卦，纳干支
创建一个天风姤卦，无动爻
```python
>>> gou = icp.Hexagram.from_binary([2, 1, 1, 1, 1, 1]) 
>>> gou
-----
-----
-----
-----
-----
-- --
```

创建一个干支装卦器，装卦
```python
>>> assigner = icp.StemBranchAssigner()
>>> assigner.assign(gou) 
>>> gou
壬 戌土 -----
壬 申金 -----
壬 午火 -----
辛 酉金 -----
辛 亥水 -----
辛 丑土 -- --
```
