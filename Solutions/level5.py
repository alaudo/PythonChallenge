import urllib.request
import pickle


data = text = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
banner = pickle.loads(data)
for line in banner:
    l = ""
    for p in line:
        l+= p[0] * p[1]
    print(l)

