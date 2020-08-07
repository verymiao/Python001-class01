# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_tag = item['movie_tag']
        movie_brief = item['movie_brief']
        output = f'{movie_name},{movie_tag},{movie_brief}\n'
        with open('./maoyan.csv','a+',encoding='utf8') as f:
            f.write(output)
        return item
