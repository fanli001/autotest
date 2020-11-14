# -*- coding: utf-8 -*-

import yaml

#读取yaml文件
with open('./lib/cases/cases.yaml',encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    
print(datas)