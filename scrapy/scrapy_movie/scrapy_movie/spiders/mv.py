import scrapy
from scrapy_movie.items import ScrapyMovieItem

class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["dytt.dytt8.net"]
    start_urls = ["https://dytt.dytt8.net/index.htm"]

    def parse(self, response):
        #//div[@class="co_content8"]//td[1]//a[2]/@href
        #//div[@class="co_content8"]//td[1]//a[2]/text()
        a_list = response.xpath('//div[@class="co_content8"]//td[1]//a[2]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            print(name ,href)
            #第二页的实际地址
            url  = 'https://dytt.dytt8.net'+href

            #对第二页链接访问
            yield scrapy.Request(url = url ,callback=self.parse_second, meta={'name':name})

    def parse_second(self, response):
        print('parsing second-page')
        src  = response.xpath('//div[@id = "Zoom"]//img/@src').extract_first()

        #接收到请求的meta参数值
        name = response.meta['name']

        movie = ScrapyMovieItem(src = src,name = name)
        print(src)

        yield movie
