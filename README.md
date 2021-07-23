# DTFmt
datetime strftime date time format strings for humans.. pythonistas

based on https://strftime.org/

## Some examples

```python
>>> from DTFmt import now_str, DTFmt
>>> now_str()
'15072021-133324'
>>> now_str(DTFmt.DMY.THIN)
'15072021'
>>> now_str(DTFmt.DMY.SPACED)
'15 07 2021'
>>> now_str(DTFmt.DMY.SLASHED)
'15/07/2021'
>>> now_str(DTFmt.YMD.SLASHED_AND_HMS_COLON)
'2021/07/15 13:35:46'
```
