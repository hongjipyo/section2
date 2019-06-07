from bs4 import *
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/courses?skill=python&order=seq/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")


recommand = soup.select(".card-content > .course_title")

#print(recommand)
i = 1
for e in recommand:
    print(i,e.string)
    i += 1
