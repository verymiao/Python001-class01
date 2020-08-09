import requests
from fake_useragent import UserAgent

#石墨文档
#https://shimo.im/lizard-api/auth/password/login
#email=23237683%40qq.com&mobile=%2B86undefined&password=23237683

ua = UserAgent(verify_ssl=False)
header = {
    'User-Agent': ua.chrome,
    'Referer':'https://shimo.im/login?from=home',
    'x-requested-with':'XmlHttpRequest'
}
from_data = {
    'email':'23237683@qq.com',
    'mobile':'+86undefined',
    'password':'23237683'
}
login_url = 'https://shimo.im/lizard-api/auth/password/login'
userInfo_url = 'https://shimo.im/lizard-api/users/me'

s = requests.Session()

response = s.post(login_url, data=from_data, headers=header)
userInfo = s.get(userInfo_url,headers=header)
print(userInfo.text)

