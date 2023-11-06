import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["search.dangdang.com"]
    start_urls = ["https://search.dangdang.com/?key=%B4%AE%C6%F0%D6%D0%B9%FA%CA%B7"]

    base_url = 'https://search.dangdang.com/?key=%B4%AE%C6%F0%D6%D0%B9%FA%CA%B7&act=input&page_index={page}'
    page = 1


    def parse(self, response):
    #src = //ul[@id="component_59"]/li//img/@src
    #alt = //ul[@id="component_59"]/li//img/@alt
    #price = //ul[@id="component_59"]/li/p/span[@class = "search_now_price"]
    #所有的selector对象都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first() #图片的懒加载反爬
            #第一张图片src可用，其他的图片地址是data-original
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()

            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('./p/span[@class = "search_now_price"]').extract_first()
            print(src,name,price)

            #item 对象
            book = ScrapyDangdangItem(src = src, name = name, price = price)

            yield book #将book交给pipelines

#每页爬取业务逻辑相同
#https://search.dangdang.com/?key=%B4%AE%C6%F0%D6%D0%B9%FA%CA%B7&act=input
#https://search.dangdang.com/?key=%B4%AE%C6%F0%D6%D0%B9%FA%CA%B7&act=input&page_index=2
#https://search.dangdang.com/?key=%B4%AE%C6%F0%D6%D0%B9%FA%CA%B7&act=input&page_index=4
        if self.page <14:
            self.page = self.page + 1
            url = self.base_url.format(page = self.page)

            #调用parse方法
            #scrapy.Request 就是scrapy的get请求
            #url为请求地址，callback为执行函数(不加括号)
            yield scrapy.Request(url = url, callback=self.parse)
