import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/sunny/?src=http%3A%2F%2Fwww.fudzilla.com%2Fmedia%2Fk2%2Fitems%2Fcache%2F78e6ada354f201704996ae31cbb3151f_L.jpg&amp;type=b400"
htmlURL = "http://google.com"

savePath1 = "C:/Users/magic/Desktop/코딩 공부/python 크롤링/자료 파일/사진/test1.jpg"
savePath2 = "C:/Users/magic/Desktop/코딩 공부/python 크롤링/자료 파일/사진/test1.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') # w,r,a
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("완료")


# urlopen과 urlretrieve 차이 :
# urlretrieve = 저장 -> open(r) -> 변수에 할당 -> 파싱 -> 저장  / 한번에 많은 자료 다운, 다이렉트
# urlopen = 변수 할당 -> 파싱 -> 저장  / 중간 작업용, 메모리
