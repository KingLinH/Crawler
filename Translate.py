import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入要翻译的内容：")
    

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15884269550837'
    data['sign'] = '651675157472924818abac69fb935995'
    data['ts'] = '1588426955083'
    data['bv'] = 'cc652a2ad669c22da983a705e3bca726'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print("翻译结果：" + target)
    time.sleep(3)
input("Press <enter>")
