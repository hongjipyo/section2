from bs4 import *
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")

url = base + quote
print(url)

res = req.urlopen(url)
savePath = "C:/Users/magic/Desktop/코딩 공부/python 크롤링/beautifulsoup4/크롤링 이미지/"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")


for i, img_list in enumerate(img_list, 1):
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)

print('완료')
