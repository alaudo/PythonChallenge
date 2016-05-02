import urllib.request

start = "90052"

while (True):
    file = open("C:\Temp\channel\\" + start + ".txt")
    text = str(file.read())
    file.close()
    print(start + " => " + str(text))
    start = str(text).strip("'").split(" ")[-1]
