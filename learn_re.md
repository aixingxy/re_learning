# 正则表达式

##  正则表达式的常用操作符
|操作符|说明|实例|
|-|-|-|
|.|表示任何单个字符| |
|[ ]|字符集，对单个字符给出取值范围|[abc]表示a、b、c，[a-z]表示a到z单个字符|
|[^ ]|非字符集，对单个字符给出排除范围|[^abc]表示非a或b或c的单个字符|
|*|前一个字符0次货无限次扩展|abc*表示ab、abc、abcc、abccc等|
|+|前一个字符1次或无限次扩展|abc+表示abc、abcc、abccc等|
|?|前一个字符0次或1次扩展|abc？表示ab、abc|
|\||左右表达式任意一个|abc\|def表示abc、def|
|{m}|扩展前一个字符m次|ab{2}c表示abbc|
|{m,n}|扩展前一个字符m至n次（含n）|ab{1,2}c表示abc、abbc|
|^|匹配字符串开头|^abc表示abc且在一个字符串的开头|
|$|匹配字符串结尾|abc$表示abc且在一个字符串的结尾|
|( )|分组标记，内部只能使用\|操作符|(abc)表示abc，(av\|def)表示abc、def|
|\d|数字，等价与[0-9]| |
|\w|单词字符，等价于[A-Za-z0-9]| |

 
## 正则表达式语法实例
```
P(Y|YT|YTH|YTHO)?N  <--->  'PN'、'PYN'、'PYTN'、'PYTHN'、'PYTHON'
PYTHON+             <--->  'PYTHON'、'PYTHONN'、'PYTHONNN'、...
PY[TH]ON            <--->  'PYTON'、'PYHON'
PY[^TH]?ON          <--->  'PYON'、'PYaON'、'PYbON'、'PYcON'、...
PY{:3}N             <--->  'PN'、'PYN'、'PYYN'、'PYYYN'
```

## 经典正则表达式实例
```
^[A-Za-z]+$            <--->  由26个字母组成的字符串
^[A-Za-z0-9]+$         <--->  由26个字母和数字组成的字符串
^-?\d$                 <--->  整数数字形式的字符串
^[0-9]*[1-9][0-9]*$    <--->  正整数形式的字符串
[1-9]\d{5}             <--->  中国境内邮政编码，6位
[\u4e00-\u9fa5]        <--->  匹配中文字符
\d{3}-\d{8}|d{4}-\d{7} <--->  国内电话号码，010-68913536
```

## Re库

re库是python的标准库，主要用于字符串匹配
```
import re
```

+ re库采用raw string类型（原生字符串类型）表示正则表达式，表示为：r‘text’
  + `r‘[1-9]\d{5}’` 
+ 原生字符串是不包含转义符的字符串

|函数|说明|
|-|-|
|re.search()|在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象|
|re.match()|从一个字符串的开始位置起匹配正则表达式，返回match对象|
|re.findall()|搜索字符串，以列表类型返回全部能匹配的子串|
|re.split()|将一个字符串按照正则表达式匹配结果进行分割，返回列表类型|
|re.finditer()|搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象|
|re.sub()|在一个字符串中替换素有匹配正则表达式的子串，返回替换后的字符串|


### re.serch(pattern, string, flags=0)
+ 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象。
  + pattern：正则表达式的字符串或原生字符串表示
  + string：待匹配字符串
  + flags：正则表达式使用时的控制标记
     |常用标记|说明|
     |-|-|
     |re.I re.IGNORECASE|忽略正则表达式的大小写，[A-A]能够匹配小写字符|
     |re.M re.MULTILINE|正则表达式中的^操作符能够将给定字符串的每行当做匹配开始|
     |re.S re.DOTALL|正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符|

```python
>>> import re
>>> match = re.search(r'[1-9]\d{5}', 'BIT 100081')
>>> if match:
...     print(match.group(0))
...
100081
```

### re.match(pattern, string, flags=0)
 + 从一个字符串的开始位置起匹配正则表达式，返回match对象
  + pattern：正则表达式的字符串或原生字符串表示
  + string：待匹配字符串
  + flags：正则表达式使用时的控制标记

```python
>>> import re
>>> match = re.match(r'[1-9]\d{5}', 'BIT 100081')
>>> if match:
...     match.group(0)
...
>>> match.group(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> match = re.match(r'[1-9]\d{5}', '100081')
>>> if match:
...     print(match.group(0))
...
'100081'
>>>
```

### re.findall(pattern, string, flags=0)
+ 搜索字符串，以列表类型返回全部能匹配的子串
  + pattern：正则表达式的字符串或原生字符串表示
  + string：待匹配字符串
  + flags：正则表达式使用时的控制标记
```python
>>> import re
>>> ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
>>> ls
['100081', '100084']
>>>
```

### re.split(pattern, string, maxsplit=0, flags=0)
+ 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
  + pattern：正则表达式的字符串或原生字符串表示
  + string：待匹配字符串
  + maxsplit：最大分割数，剩余部分最为最后一个元素输出
  + flags：正则表达式使用时的控制标记
```python
>>> import re
>>> re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
['BIT', ' TSU', '']
>>> re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
['BIT', ' TSU100084']
```

### re.finditer(pattern, string, flags=0)
+ 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
  + pattern：正则表达式的字符串或原生字符串表示
  + string：待匹配字符串
  + flags：正则表达式使用时的控制标记
```python
>>> import re
>>> for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
...     if m:
...             print(m.group(0))
...
100081
100084
```

### re.sub(pattern, repl, string, count=0, flags=0)
+  在一个字符串中替换素有匹配正则表达式的子串，返回替换后的字符串
  + pattern：正则表达式的字符串或原生字符串表示
  + repl：替换匹配字符串的字符串
  + string：待匹配字符串
  + count：匹配的最大提花次数
  + flags：正则表达式使用时的控制标记
```python
>>> import re
>>> re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
'BIT:zipcode TSU:zipcode'
```

## Re库的另一种等价用法
面向对象用法：编译后的多次操作
```python
>>> import re
>>> pat = re.compile(r'[1-9]\d{5}')
>>> rst = pat.search('BIT 100081')
>>> rst.group(0)
'100081'
```

这种方式的好处是经过一次编译，当需要用到正则表达式匹配时，可以加快程序运行。
### regex = re.compile(pattern, flags=0)
+ 将正则表达式的字符串形式编译成正则表达式对象
  + pattern：正则表达式的字符串或原生字符串表示
  + flags：正则表达式使用时的控制标记

|函数|说明|
|-|-|
|regex.search()|在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象|
|regex.match()|从一个字符串的开始位置起匹配正则表达式，返回match对象|
|regex.findall()|搜索字符串，以列表类型返回全部能匹配的子串|
|regex.split()|将一个字符串按照正则表达式匹配结果进行分割，返回列表类型|
|regex.finditer()|搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象|
|regex.sub()|在一个字符串中替换素有匹配正则表达式的子串，返回替换后的字符串|

## math对象
```python
>>> import re
>>> match = re.search(r'[1-9]\d{5}', 'BIT 100081')
>>> if match:
...     print(match.group(0))
...
100081
>>> type(match)
<class '_sre.SRE_Match'>
```

match对象的属性
|属性|说明|
|-|-|
|.string|待匹配的文本|
|.re|匹配时使用的pattern对象（正则表达式）|
|.pos|正则表达式搜索文本的开始位置|
|.endpos|正则表达式搜索文本的结束位置|

match对象的方法
|方法|说明|
|-|-|
|.group(0)|获得匹配后的字符串|
|.start()|匹配字符串在原始字符串的开始位置|
|.end()|匹配字符串在原始字符串的结束位置|
|.span()|返回(.start(), .end())|

```python
>>> import re
>>> m = re.search(r'[1-9]\d{5}', 'BIT 100081')
>>> m.string
'BIT 100081'
>>> m.re
re.compile('[1-9]\\d{5}')
>>> m.pos
0
>>> m.endpos
10
>>> m.group(0)  # 如果要返回每个结果，需要使用finditer
'100081'
>>> m.start()
4
>>> m.end()
10
>>> m.span()
(4, 10)
```

## Re库的贪婪匹配和最小匹配
+ 贪婪匹配实例
```python
>>> import re
>>> match = re.search(r'PY.*N', 'PYANBNCNDN')
>>> match.group(0)
'PYANBNCNDN'
```
Re库默认采用贪婪匹配，即输出匹配最长的子串

+ 贪婪匹配实例
```python
>>> match = re.search(r'PY.*?N', 'PYANBNCNDN')
>>> match.group(0)
'PYAN'
```

最小匹配操作符

|属性|说明|
|-|-|
|*?|前一个字符0次或无限次扩展，最小匹配|
|+?|前一个字符1次或无线次扩展，最小匹配|
|??|前一个字符0次或1次扩展，最小匹配|
|{m,n}?|扩展前一个字符m至n次（含n），最小匹配|


