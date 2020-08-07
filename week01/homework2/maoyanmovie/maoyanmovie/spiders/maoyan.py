# -*- coding: utf-8 -*-
import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        for movie in movies:
            item = MaoyanmovieItem()
            item['movie_name'] = movie.xpath('./div[2]/a/div/div[1]/span[1]/text()').get().strip()
            item['movie_tag'] = movie.xpath('./div[2]/a/div/div[2]/text()[2]').get().strip()
            item['movie_brief'] = movie.xpath('./div[2]/a/div/div[4]/text()[2]').get().strip()
            yield item
