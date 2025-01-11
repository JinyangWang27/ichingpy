# Sexagenary Cycle (天干地支)

```python
import ichingpy as icp
icp.HeavenlyStem.Jia + 1
#> <HeavenlyStem.Yi: 2>
```

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
jia_zi + jia_zi
#> 乙丑
```