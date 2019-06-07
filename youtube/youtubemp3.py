import pytube
import subprocess # 커맨드 창에 입력, 반환
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print("URL 주소 입력")
url = input()

yt = pytube.YouTube(url)
videos = yt.streams.all()

print('videos', videos)

for i in range(len(videos)):
    print(i,',', videos[i])

print("다운 받을 화질은?(0~21 입력) *0 권장")
cNum = int(input())

down_dir = "C:/Users/magic/Desktop/코딩 공부/python 크롤링/youtube"

videos[cNum].download(down_dir)

print("변환 할 파일명은?")

newFileName = input()
oriFileName = videos[cNum].default_filename
delFileName = oriFileName + '.mp4'


subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName),

])

subprocess.call('del','/p',os.path.join(down_dir,delFileName))
