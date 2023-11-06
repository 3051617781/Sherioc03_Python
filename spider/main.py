from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
#get方法会一直等到页面被完全加载，然后才会执行程序，通常测试会选择执行time.sleep(2)
driver.get("https://www.dangdang.com")
driver.implicitly_wait(5)#【全局】隐式等待，一个元素最多等5s，期间一直轮询查找定位元素
time.sleep(2) #等待页面完全加载 

key = driver.find_element(By.ID,'key_S')
words = ['小说','科幻','计算机']

key.send_keys(words[0])

time.sleep(1)
search = driver.find_element(By.CSS_SELECTOR,".search .button")
search.click()

time.sleep(2)
for i in range(4):
    print('\n')
    shoplist = driver.find_elements(By.CSS_SELECTOR, ".shoplist li")
    for li in shoplist:
        print(li.find_element(By.CSS_SELECTOR,"a").get_attribute("title"))
        with open('main.txt','a',encoding='utf-8')as f:
            writer = csv.writer(f)
            writer.writerow(['张三','男','14'])

    js = "window.scrollTo(0,8000)"
    driver.execute_script(js) #执行滚动js代码

    time.sleep(2)
    try:
        next = driver.find_element(By.LINK_TEXT,"下一页") #通过链接文本找
        next.click()
    except:
        driver.get_screenshot_as_file('wrong.png') #执行出错时候获取窗口截图
    

