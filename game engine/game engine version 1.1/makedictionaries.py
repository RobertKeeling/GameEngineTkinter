dicnames = ["idic = {","bgdic = {","ildic = {","spritedic = {"]
filenames = ["items.py","backgrounds.py","itemlocales.py","sprites.py"]
f = ""
for i in range(4):
    file = open(filenames[i],"r")
    x = file.readlines()
    s = ""
    for l in x:
        n = l.split("=")[0][:-1]
        s += "\""+n+"\":"+n+","
    f += dicnames[i]+s[:-1]+"}\n"

f = "from items import *\nfrom backgrounds import *\nfrom sprites import *\nfrom itemlocales import *\n\n"+f

file = open("dictionaries.py","w")
file.write(f)
file.close()
