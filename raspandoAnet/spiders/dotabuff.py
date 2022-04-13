from urllib import response
import scrapy


class DotabuffSpider(scrapy.Spider):
    name = 'dotabuff'    
    start_urls = ['https://pt.dotabuff.com/heroes/meta']

    def parse(self, response):      
      
        for meta in response.css('.link-type-hero'):
             yield{
                   'heroi':meta.css('.link-type-hero::text').get(),
                   'winRate':response.css('.r-group-1::text').getall(),
             }
        