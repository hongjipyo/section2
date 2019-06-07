import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.naver.com"

mem = req.urlopen(url)

#print("geturl", mem.geturl())
#print("status", mem.status) # 200 : 정상, 404 : 페이지 X, 403 : 외부 접속 불가, 500 : 서버 에러
#print("headers", mem.getheaders())
#print("------------------")
#print("info", mem.info())
#print("code", mem.getcode())
#print("read", mem.read(50).decode("utf-8")) # 숫자값에 따라 가져올양 정함, decode값 으로 정함
print(urlparse("http://www.naver.com?test=test"))

#print(type(mem))
#print(type({}))
#print(type([]))
#print(type(()))
