#!/usr/bin/env python3
#
#爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间
import requests
import lxml.etree
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = '__mta=121476535.1595409959948.1595473415661.1595473431126.7; uuid_n_v=v1; uuid=57DF0720CBFD11EABDA91DE1C2FF6305554804AEB9CC4103A004A7D5A148B17D; _lxsdk_cuid=17375d805df5b-03f4c48df5c205-4353760-384000-17375d805e063; _lxsdk=57DF0720CBFD11EABDA91DE1C2FF6305554804AEB9CC4103A004A7D5A148B17D; mojo-uuid=a92e94e25cd132155d59982d03de1f5b; _csrf=427e9581e275cfac302bd6ed538a355178b8f5dac76e5c67b1957ed80b5b8283; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595419299,1595419341,1595470608,1595844742; mojo-session-id={"id":"664d715f83dd9d0c438a994fb0f0d909","time":1595864765409}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595866309; __mta=121476535.1595409959948.1595473431126.1595866309587.8; _lxsdk_s=17390f3ca72-2da-a3f-720%7C%7C4'
header = {'User-Agent': user_agent,
          'Cookie': cookie}
url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=header)
selector = lxml.etree.HTML(response.text)
movies_list = []
for movie in selector.xpath('//div[@class="movie-item film-channel"]'):
    movie_name = movie.xpath('./div[2]/a/div/div[1]/span[1]/text()')[0].strip()
    movie_tag = movie.xpath('./div[2]/a/div/div[2]/text()[2]')[0].strip()
    movie_brief = movie.xpath('./div[2]/a/div/div[4]/text()[2]')[0].strip()
    #print(f'{movie_name},{movie_tag},{movie_brief}')
    movie_list = [movie_name, movie_tag, movie_brief]
    movies_list.append(movie_list)

#print(movies_list)
maoyan = pd.DataFrame(data=movies_list[0:10])
maoyan.to_csv('./maoyan.csv', encoding='utf8', index=False, header=False)

