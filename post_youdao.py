import requests

url="http://fanyi.youdao.com/translate o？smartresult=dict&smartresult=rele"
form_data={
  'i': '葵司you',
  'from': 'AUTO',
  'to': 'AUTO',
  'smartresult': 'dict',
  'client': 'fanyideskweb',
  'salt': '15846844587184',
  'sign': '46b98940452b704f9b97929473c4b0ef',
  'ts': '1584684458718',
  'bv': '0ed2e07b89acaa1301d499442c9fdf79',
  'doctype': 'json',
  'version': '2.1',
  'keyfrom': 'fanyi.web',
  'action': 'FY_BY_REALTlME'
}
response=requests.post(url,form_data)
print(response.text)