import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/sunny/?src=http%3A%2F%2Fwww.fudzilla.com%2Fmedia%2Fk2%2Fitems%2Fcache%2F78e6ada354f201704996ae31cbb3151f_L.jpg&amp;type=b400"
htmlURL = "http://google.com"

savePath1 = "C:/Users/magic/Desktop/코딩 공부/python 크롤링/자료 파일/사진/test1.jpg"
savePath2 = "C:/Users/magic/Desktop/코딩 공부/python 크롤링/자료 파일/사진/test1.html"

dw.urlretrieve(imgUrl, savePath1) #(경로, 저장경로)
dw.urlretrieve(htmlURL, savePath2) #페이지의 html문서 출력

print("완료")
