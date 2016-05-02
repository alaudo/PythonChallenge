import urllib.request

start = "1234"

while (True):
    text = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + start).read()
    print(start + " => " + str(text))
    start = str(text).strip("'").split(" ")[-1]
