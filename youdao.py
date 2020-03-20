import requests

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
from_data = {
    'i': '我和你',
    'from': 'AUTO',
    print(response.text)    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15846844488375',
    'sign': '51a801838d8e15397ff4f501eadf5c1b',
    'ts': '1584684448837',
    'bv': '0ed2e07b89acaa1301d499442c9fdf79',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response = requests.post(url, from_data)
