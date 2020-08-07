#!/usr/bin/env python3

#爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间
"""
电影名称: <div class="channel-detail movie-item-title" title="釜山行2：半岛">
      <a href="/films/1297466" target="_blank" data-act="movies-click" data-val="{movieId:1297466}">釜山行2：半岛</a>
    </div>
电影类型: <div class="movie-hover-title" title="釜山行2：半岛">
             <span class="hover-tag">类型:</span>
             动作／惊悚
           </div>
上映时间: <div class="movie-hover-title movie-hover-brief" title="釜山行2：半岛">
              <span class="hover-tag">上映时间:</span>
              2020-08-12
            </div>
"""
import requests
import re

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=57DF0720CBFD11EABDA91DE1C2FF6305554804AEB9CC4103A004A7D5A148B17D; _csrf=21f030fe4f184e90926101c94b69660a42051fe8c2ab06663b5170fdb0b629da; _lxsdk_cuid=17375d805df5b-03f4c48df5c205-4353760-384000-17375d805e063; _lxsdk=57DF0720CBFD11EABDA91DE1C2FF6305554804AEB9CC4103A004A7D5A148B17D; mojo-uuid=a92e94e25cd132155d59982d03de1f5b; mojo-session-id={"id":"637f60ba52694426582d0af3c5d6d84c","time":1595419298952}; __mta=121476535.1595409959948.1595409959948.1595419299774.2; mojo-trace-id=2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595409958,1595419299,1595419341; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595419341; _lxsdk_s=17376668e4e-dcc-9b-891%7C%7C3'

header = {'User-Agent': user_agent,
          'Cookie': cookie}
url = 'https://maoyan.com/films?showType=3'

content = requests.get(url,headers=header).text
pattern = re.compile(r'<div class="movie-hover-title" title="(.*?)".*?类型:</span>(.*?)</div>.*?上映时间:</span>(.*?)</div>', re.S)
results = re.findall(pattern, content)

num = 1
for result in results:
    if num > 10:
        break
    name, tag, brief = result
    list1 = [name, newtag, newbrief]
    #csv = list(name,re.sub('\s', '', tag), re.sub('\s', '', brief))
    print(list1)
    with open('maoyan.csv','a+',encoding='utf8') as f:
        f.write('%s,%s,%s\n' %(name, re.sub('\s', '', tag), re.sub('\s', '', brief)))
    num += 1
    #print(name,re.sub('\s', '', tag), re.sub('\s', '', brief))


