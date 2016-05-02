f = open("level2.txt")
line = f.read()
print("".join([a if str.isalpha(a) else "" for a in line]))
