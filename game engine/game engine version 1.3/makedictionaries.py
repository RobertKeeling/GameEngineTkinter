dicnames = ["idic = {","bgdic = {","ildic = {","spritedic = {"]
filenames = ["items.py","backgrounds.py","itemlocales.py","sprites.py"]
prefixes = ["items.","backgrounds.","itemlocales.","sprites."]
f = ""
for i in range(4):
    file = open(filenames[i],"r")
    x = file.readlines()
    s = ""
    for l in x:
        n = l.split("=")[0][:-1]
        s += "\""+n+"\":"+prefixes[i]+n+","
    f += dicnames[i]+s[:-1]+"}\n"

fi = "import importlib\nimport items\nimport backgrounds\nimport sprites\nimport itemlocales\n\n"
fi += "importlib.reload(items)\nimportlib.reload(backgrounds)\nimportlib.reload(sprites)\nimportlib.reload(itemlocales)\n"
f = fi+f

file = open("dictionaries.py","w")
file.write(f)
file.close()

def fg():
    dicnames = ["idic = {","bgdic = {","ildic = {","spritedic = {"]
    filenames = ["items.py","backgrounds.py","itemlocales.py","sprites.py"]
    prefixes = ["items.","backgrounds.","itemlocales.","sprites."]
    f = ""
    for i in range(4):
        file = open(filenames[i],"r")
        x = file.readlines()
        s = ""
        for l in x:
            n = l.split("=")[0][:-1]
            s += "\""+n+"\":"+prefixes[i]+n+","
        f += dicnames[i]+s[:-1]+"}\n"

    fi = "import importlib\nimport items\nimport backgrounds\nimport sprites\nimport itemlocales\n\n"
    fi += "importlib.reload(items)\nimportlib.reload(backgrounds)\nimportlib.reload(sprites)\nimportlib.reload(itemlocales)\n"
    f = fi+f

    file = open("dictionaries.py","w")
    file.write(f)
    file.close()
