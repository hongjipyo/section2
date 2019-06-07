import pytube
import subprocess # 커맨드 창에 입력, 반환
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


yt = pytube.YouTube("https://www.youtube.com/watch?v=RC7veMauJLo")
videos = yt.streams.all()

print('videos', videos)

for i in range(len(videos)):
    print(i,',', videos[i])

cNum = int(input("다운 받을 화질은?(0~21 입력)"))

down_dir = "C:/Users/magic/Desktop/코딩 공부/python 크롤링/youtube"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName),
])
