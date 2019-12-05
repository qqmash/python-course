from urllib.request import urlopen
s = urlopen("https://www.w3.org/TR/PNG/iso_8859-1.txt").read()
print(s)
