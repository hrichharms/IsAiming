import os
from PIL import Image
from datetime import datetime

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
            if limg[i, j][0] >= 170 and limg[i, j][1] <= 100 and limg[i, j][2] <= 100:
                limg[i, j] = (255, 255, 255)
            else:
                limg[i, j] = (0, 0, 0)
    img.save(ofile)

s = datetime.now()
for i in range(n):
    process(filtered[i], processed[i])
    if i % 1000 == 0: print(str(round(i / n * 100, 2)) + "% finished")
print(datetime.now() - s)
