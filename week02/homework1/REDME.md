## 代理IP功能
~~~
代理IP来源: http://www.66ip.cn/areaindex_1/1.html

setting.py
DOWNLOADER_MIDDLEWARES = {
   'maoyanmovie.middlewares.MaoyanmovieDownloaderMiddleware': 543,
   'maoyanmovie.middlewares.RandomHttpProxyMiddleware': 400,
}
HTTP_PROXY_LIST = [
   'http://39.156.51.7:8080',
   'http://101.4.136.34:81',
]

~~~
## 保存到MySQL
~~~
mysql使用虚拟安装,运行代码正常
~~~