from lxml import etree
import urllib.request
'''
1.路径查询
//查找所有子孙节点
/ 查找所有子节点

2.谓词查询
//div[@id="id_name"] 所有id为id_name的标签

3.属性查询
//@class
//@value

4.模糊查询
//div[contains(@id,"he")]
//div[starts-with(@id,"he")]

5.内容查询
//div/h1/text()

6.逻辑运算
//div[@id="head" and @class="s"]
//title | //price
'''

url = 'https://www.baidu.com'
def headers():
    Headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Cookie':'BIDUPSID=BF80D5E626950DDCC8CC51FA67C54520; PSTM=1675175661; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=VaaUI3dUdLfn41d1hHQTNqdU9mMU0xWTBOTUwtWXF2S1JKY0ptZnE5eVZsRHRrSVFBQUFBJCQAAAAAAQAAAAEAAACdqoNns7XHsLLd1NqztcewAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJUHFGSVBxRkUX; BDUSS_BFESS=VaaUI3dUdLfn41d1hHQTNqdU9mMU0xWTBOTUwtWXF2S1JKY0ptZnE5eVZsRHRrSVFBQUFBJCQAAAAAAQAAAAEAAACdqoNns7XHsLLd1NqztcewAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJUHFGSVBxRkUX; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1681397830; BAIDUID=CEFC652A1902C90FA49B46C4F2C55549:FG=1; BAIDUID_BFESS=CEFC652A1902C90FA49B46C4F2C55549:FG=1; APPGUIDE_10_6_6=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1699009689; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1699009779; ab_sr=1.0.1_NTc0MjExNTU5ZjViNTNiMDFmMzc5YWJkMjBjODQzMTRlNjEwNjJkYTQ5NzFkMjZiM2RjNmE0OGUwZTJmNmFlZmYzYzM2Mjg0MWUyYjczODFjYzE4NGNiNzk5YjVjMWRkNGE0ZWVjNmQyYmI3ODg2ZmQwOTY1OWE1NDgyYTNiNWNlYmVlYWRiM2YxYWYzMmRjMWY3NzlhYjQyNjYwMTZhMzcwZWFlMzZhNTI2MGYwYjA0NTFmYmVlMzM0NjNkMzIy'
    }
    return Headers
def xpath_use():
    request = urllib.request.Request(url,headers= headers()) #定制请求对象
    response = urllib.request.urlopen(request) #获取响应
    content  = response.read().decode() #获取网页源码
    tree = etree.HTML(content) #解析服务器响应的文件
    result = tree.xpath('//input[@id="su"]/@value')
    print(result) #['百度一下']

if __name__ == '__main__':
    xpath_use()