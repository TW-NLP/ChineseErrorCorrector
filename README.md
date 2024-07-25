#  一键语法错误增强工具

使用：`pip install ChineseErrorCorrector`

开源不易，欢迎 star🌟

pypi:https://pypi.org/project/ChineseErrorCorrector/

---

## 介绍

一键语法错误增强工具，支持：
- [1.缺字漏字](#1缺字漏字)
- [2.错别字错误](#2错别字错误)
- [3.缺少标点](#3缺少标点)
- [4.错用标点](#4错用标点)
- [5.主语不明](#5主语不明)
- [6.谓语残缺](#6谓语残缺)
- [7.宾语残缺](#7宾语残缺)
- [8.其他成分残缺](#8其他成分残缺)
- [9.虚词多余](#9虚词多余)
- [10.其他成分多余](#10其他成分多余)
- [11.主语多余](#11主语多余)
- [12.语序不当](#12语序不当)
- [13.动宾搭配不当](#13动宾搭配不当)
- [14.其他搭配不当](#14其他搭配不当)




## 注意

如果没有进行数据增强，则返回None

---
## API



### 1.缺字漏字


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.lack_word("小明住在北京"))

```
### 2.错别字错误


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.wrong_word("小明住在北京"))

```
### 3.缺少标点


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.lack_char("小明住在北京"))


```
### 4.错用标点


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.wrong_char("小明住在北京"))

```
### 5.主语不明


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.unknow_sub("小明住在北京"))

```
### 6.谓语残缺


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.unknow_pred("小明住在北京"))

```
### 7.宾语残缺


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.lack_obj("小明住在北京"))

```
### 8.其他成分残缺


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.lack_others("小明住在北京"))

```
### 9.虚词多余

```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.red_sub("小明住在北京"))

```
### 10.其他成分多余


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.red_component("小明住在北京"))

```
### 11.主语多余


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.red_sub("小明住在北京"))

```


### 12.语序不当


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.wrong_sentence_order("小明住在北京"))


```




### 13.动宾搭配不当


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.wrong_ver_obj("小明住在北京"))


```


### 14.其他搭配不当


```python
from ChineseErrorCorrector.dat import GrammarErrorDat

cged_tool = GrammarErrorDat()
print(cged_tool.other_wrong("小明住在北京"))


```


