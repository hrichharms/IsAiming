import os
from PIL import Image

cwd = os.getcwd()
filtered = [cwd + "/Data/FILTERED/" + i for i in os.listdir("Data/FILTERED")]
processed = [cwd + "/Data/PROCESSED/" + i for i in os.listdir("Data/FILTERED")]
n = len(filtered)

def process(ifile, ofile):
    img = Image.open(ifile)
    w, h = img.size
    limg = img.load()
    for i in range(w):
        for j in range(h):
            r = limg[i, j][0]
            limg[i, j] = (r, r, r)
    img.save(ofile)

for i in range(n):
    process(filtered[i], processed[i])
    if i % 1000 == 0: print(str(round(i / n * 100, 2)) + "% finished")
