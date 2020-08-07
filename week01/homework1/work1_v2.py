#!/usr/bin/env python3
#
#爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = '__mta=121476535.1595409959948.1595473415661.1595473431126.7; uuid_n_v=v1; uuid=57DF0720CBFD11EABDA91DE1C2FF6305554804AEB9CC4103A004A7D5A148B17D; _csrf=21f030fe4f184e90926101c94b69660a42051fe8c2ab06663b5170fdb0b629da; _lxsdk_cuid=17375d805df5b-03f4c48df5c205-4353760-384000-17375d805e063; _lxsdk=57DF0720CBFD11EABDA91DE1C2FF6305554804AEB9CC4103A004A7D5A148B17D; mojo-uuid=a92e94e25cd132155d59982d03de1f5b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595409958,1595419299,1595419341,1595470608; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595473447; __mta=121476535.1595409959948.1595473431126.1595473447926.8; _lxsdk_s=1737a099f72-445-c73-d23%7C%7C1'
header = {'User-Agent': user_agent,
          'Cookie': cookie}
url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=header)
#bs_info = BeautifulSoup(response.text, 'html.parser')
bs_info = BeautifulSoup(response.text, 'lxml')

#print(bs_info)

num = 1
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    if num > 10:
        break
    movie_name = tags.find('span').text
    nnum = 1
    for dtag in tags.find_all('div'):
        if nnum == 2:
            movie_tag = dtag.find('span').next.next.strip()
        elif nnum == 4:
            movie_brief = dtag.find('span').next.next.strip()
        nnum += 1
    #print('%s,%s,%s\n' %(movie_name, movie_tag, movie_brief))
    with open('movies.csv','a+',encoding='utf8') as f:
        f.write('%s,%s,%s\n' %(movie_name, movie_tag, movie_brief))
    num += 1

