from bs4 import *
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1>파이썬 Beautifulsoup4 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
""" #줄바꿈 포함 문자열

soup =BeautifulSoup(html,'html.parser')

#print('soup', type(soup))

#print('prettify', soup.prettify()) #라인 정리 => prettify

h1 = soup.html.body.h1

#print(h1) # 라인 전체
#print(h1.string) # 문자만

#next_sibling : 다음 노드 이동
#previous_sibling : 이전 노드 이동
#next_sibling 썼을때 나오지 않는이유 : 줄바꿈을 인식 했기 때문

p1 = soup.body.p
p2 = p1.next_sibling.next_sibling
p3 = p1.previous_sibling.previous_sibling

print(p1.string)
print(p2.string)
print(p3.string)
