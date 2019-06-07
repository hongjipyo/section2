from bs4 import *
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
    <body>
        <ul>
            <li><a href="http://www.naver.com">naver</a></li>
            <li><a href="http://www.daum.net">daum</a></li>
            <li><a href="http://www.daum.com">daum</a></li>
            <li><a href="http://www.google.com">google</a></li>
            <li><a href="http://www.tistory.com">tistory</a></li>
        </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify)

link = soup.find_all("a")

#a = soup.find_all("a", string='daum') # find_all = 전부 가져옴
#b = soup.find("a") # 상위 1개만 가져옴
#c = soup.find_all("a", limit=3) # limit 개수만큼 가져옴
#d = soup.find_all(string=["naver","google"]) # 해당 문자열 가져옴

#print(a)
#print(b)
#print(c)
#print(d)

#print('link', type(link))

for a in link:
    #print('a', type(a),a)
    href = a.attrs['href']
    txt = a.string
    #print('txt >>',txt,'href >>', href)
