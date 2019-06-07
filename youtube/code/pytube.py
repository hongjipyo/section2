from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=RC7veMauJLo').streams.first().download()
