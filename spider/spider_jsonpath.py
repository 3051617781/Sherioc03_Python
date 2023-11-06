import jsonpath
import json
obj = json.load(open('./data/jsonpath.json','r',encoding='utf-8'))
list = jsonpath.jsonpath(obj,'')