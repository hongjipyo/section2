 from bs4 import *
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open('C:/Users/magic/Desktop/코딩 공부/python 크롤링/beautifulsoup4/car.html',encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars > #gr")
car_func("li[id='gr']")
car_func("li:nth-of-type(4)")

print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")
car_lambda("li:nth-of-type(4)")
