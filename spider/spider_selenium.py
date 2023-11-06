from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

def index():
    print('start crawl')
    lis = driver.find_elements(By.CLASS_NAME ,"job-card-wrapper")
    print(lis)
    print('====')
    for li in lis:
        print('li in lis------')

        title = li.find_element(By.CLASS_NAME ,"job-name").text
        area = li.find_element(By.CLASS_NAME ,"job-area").text
        salary = li.find_element(By.CLASS_NAME ,"salary").text
        tag = li.find_element(By.CLASS_NAME ,"tag-list").text
        company = li.find_element(By.CLASS_NAME ,"company-name").text
        commpany_type = li.find_element(By.CLASS_NAME ,"company-tag-list").text
        print(title, area, salary, tag, company, commpany_type)
        csv.writer(f).writerow([title, area, salary, tag, company, commpany_type]) 
        
        print('li in lis########')

f = open("boos直聘.csv", "w", encoding="utf-8", newline="")
csv.writer(f).writerow(["职位", "位置", "薪资", "经验", "公司名", "类型"])

driver = webdriver.Chrome()
driver.get("https://www.zhipin.com/")
print('---------------')

time.sleep(3)
# 输入搜索内容
driver.find_element(By.CSS_SELECTOR ,".ipt-search").send_keys("ai")
time.sleep(5)
# 模拟回车键
driver.find_element(By.CSS_SELECTOR ,".ipt-search").send_keys(Keys.ENTER)
time.sleep(8)
index()
print('########')
driver.quit()