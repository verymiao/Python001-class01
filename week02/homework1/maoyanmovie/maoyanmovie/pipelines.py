# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_tag = item['movie_tag']
        movie_brief = item['movie_brief']
        data = [(movie_name, movie_tag, movie_brief)]
        #print(f'{data}')
        sql = 'INSERT INTO maoyan(movie_name, movie_tag, movie_brief) values (%s,%s,%s);'
        try:
            db = pymysql.connect(host='192.168.77.77', port=3306, user='root', passwd='mysql123', database='maoyan',
                                 charset='utf8mb4')
            cur = db.cursor()
            cur.executemany(sql, data)
            db.commit()
        except Exception as error:
            db.rollback()
        finally:
            cur.close()
            db.close()
        # output = f'{movie_name},{movie_tag},{movie_brief}\n'
        # with open('./maoyan.csv','a+',encoding='utf8') as f:
        #     f.write(output)

        return item
