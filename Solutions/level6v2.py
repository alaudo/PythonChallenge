import zipfile

zf = zipfile.ZipFile('c:\\temp\channel.zip', 'r')

start = "90052"

line = ""

while (True):
    file = zf.open(start + ".txt")
    info = zf.getinfo(start + ".txt")
    text = str(file.read())
    line += info.comment.decode("utf-8") 
    if (info.comment == b'\n'):
        print(line)
        line = ""
    file.close()
    ##print(start + " => " + str(text))
    start = str(text).strip("'").split(" ")[-1]


