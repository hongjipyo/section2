import urllib

class sample:
    def __init__(self, x):
        self.x = x

urllib.parse = sample(1)
urllib.parse.x

hasattr(urllib.parse, 'urlencode')
