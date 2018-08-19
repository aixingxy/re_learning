# -*- coding:utf-8 -*-

import requests

url = 'http://124.126.15.169:8081/cx/api/cxsj/syscqyinfo/detail/27051?_=1534599732473'
res = requests.json(url)
print(res)