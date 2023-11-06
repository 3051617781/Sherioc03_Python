import urllib.request #urllib_spider
import urllib.parse 
import json
import random
#反爬处理/Chrome
def headers():
    Headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Cookie':'BIDUPSID=BF80D5E626950DDCC8CC51FA67C54520; PSTM=1675175661; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=VaaUI3dUdLfn41d1hHQTNqdU9mMU0xWTBOTUwtWXF2S1JKY0ptZnE5eVZsRHRrSVFBQUFBJCQAAAAAAQAAAAEAAACdqoNns7XHsLLd1NqztcewAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJUHFGSVBxRkUX; BDUSS_BFESS=VaaUI3dUdLfn41d1hHQTNqdU9mMU0xWTBOTUwtWXF2S1JKY0ptZnE5eVZsRHRrSVFBQUFBJCQAAAAAAQAAAAEAAACdqoNns7XHsLLd1NqztcewAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJUHFGSVBxRkUX; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1681397830; BAIDUID=CEFC652A1902C90FA49B46C4F2C55549:FG=1; BAIDUID_BFESS=CEFC652A1902C90FA49B46C4F2C55549:FG=1; APPGUIDE_10_6_6=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1699009689; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1699009779; ab_sr=1.0.1_NTc0MjExNTU5ZjViNTNiMDFmMzc5YWJkMjBjODQzMTRlNjEwNjJkYTQ5NzFkMjZiM2RjNmE0OGUwZTJmNmFlZmYzYzM2Mjg0MWUyYjczODFjYzE4NGNiNzk5YjVjMWRkNGE0ZWVjNmQyYmI3ODg2ZmQwOTY1OWE1NDgyYTNiNWNlYmVlYWRiM2YxYWYzMmRjMWY3NzlhYjQyNjYwMTZhMzcwZWFlMzZhNTI2MGYwYjA0NTFmYmVlMzM0NjNkMzIy'
    }
    return Headers

#使用urllib
def urllib_request():
    url = 'https://www.baidu.com'
    request = urllib.request.Request(url, headers=headers())#定制请求对象request
    
    data = {
        'name':'张杰',
        'sex':'男'
    }
    data = urllib.parse.urlencode(data) #将data对象变为unicode编码 name=%E5%BC%A0%E6%9D%B0&sex=%E7%94%B7

    response = urllib.request.urlopen(request) # urllib.request.urlretrieve(url,'baidu.html') #下载网页/图片
    # content = response.read().decode() #read返回字节形式的二进制数据,decode指定编码
    print(type(response),response.getcode(),response.geturl(),response.getheaders()) #HTTPResponse、响应码、url、响应头

#post请求发送表单数据
def urllib_post():
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 'baidu',
        'simple_means_flag':'3' ,
        'sign': '430944.159825',
        'token': '3001b23d9bf04576ac5351636f87054c',
        'domain': 'common',
        'ts': '1699009779912'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')#post请求参数必须编码
    request = urllib.request.Request(url=url,data=data,headers=headers())

    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    obj = json.loads(content)
    # print(obj)

#爬取豆瓣start-end页的电影
def urllib_ajax():
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={start}&limit=20'
    start_page = int(input('enter the first page:'))
    end_page = int(input('enter the end page:'))
    for i in range(start_page, end_page+1):
        url = base_url.format(start = (i-1)*20)
        request = urllib.request.Request(url = url, headers= headers())
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        #open默认使用gbk，保存汉字使用utf-8
        with open('./data/douban{i}.json'.format(i = i),'w',encoding='utf-8')as f:
            f.write(content)

#urllib代理    
def handler_request():
    url = 'https://baidu,com'
    proxies_pool = [{'http':'183.236.232.160'}]
    proxies = random.choice(proxies_pool)
    request = urllib.request.Request(url = url, headers=headers())
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf-8')

if __name__ == '__main__':
    #使用urllib
    # urllib_request()
    # urllib_post()
    # urllib_ajax()
    handler_request()