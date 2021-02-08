import os
from PIL import Image
from shutil import copyfile

def list_images(a):
    return [i for i in os.listdir(a) if i.split(".")[1] == "png"]

def is_data(a, sample_coords, data_color):
    x, y = sample_coords
    d_r, d_g, d_b = data_color
    im = Image.open(a)
    try:
        r, g, b = im.load()[x, y]
        #print(r, g, b)
    except OSError:
        return False
    if r == d_r and g == d_g and b == d_b:
        return True
    else:
        return False

if __name__ == "__main__":
    SAMPLE_COORDS = (48, 40)
    DATA_COLOR = (0, 0, 0)

    s_directory = os.getcwd()
    os.chdir("Data")

    filtered = []
    for session in os.listdir():
        filtered.extend([s_directory + "/Data/" + session + "/" + i for i in os.listdir(session) if is_data(s_directory + "/Data/" + session + "/" + i, SAMPLE_COORDS, DATA_COLOR)])

    for file in filtered:
        copyfile(file, s_directory + "/Data/FILTERED/" + file.split("/")[-1])
