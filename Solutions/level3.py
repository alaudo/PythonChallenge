import re

line = open("level3.txt").read()
rx = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")
print("".join(rx.findall(line)))

