# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


#如果使用管道，必须在settings中开启
class ScrapyDangdangPipeline:

    def open_spider(self,spider):
        self.fp = open('book.json','w',encoding='utf-8')
    # item为yield传来的对象

    def process_item(self, item, spider):

        self.fp.write(str(item))
        
        return item

    def close_spider(self,spider):
        self.fp.close()

#多管道
#（1）定义管道类
#（2）在settings中开启管道
#  "scrapy_dangdang.pipelines.DangDangPipeline": 301,

import urllib.request
class DangDangPipeline:
    def process_item(self, item, spider):
        #使用urllib.request.urlretrieve(url = url, filename=filename)下载图片

        url = 'http:'+item.get('src')
        filename = './books/'+item.get('name')+'.jpg'

        return item