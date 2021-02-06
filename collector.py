from PIL import ImageGrab
from random import randint
from time import sleep
from socket import gethostname
from datetime import datetime

SLEEP_LOWER, SLEEP_UPPER = [3, 5]
WIDTH, HEIGHT = ImageGrab.grab().size
HOSTNAME = gethostname()

def screenshot():
    im = ImageGrab.grab(bbox=(WIDTH // 2 - 50, HEIGHT // 2 - 50, WIDTH // 2 + 50, HEIGHT // 2 + 50))
    time_component = str(datetime.now()).split(".")[0].replace(":", "")
    im.save("Data/" + HOSTNAME.replace("-", "") + "_" + time_component + ".png")

while True:
    screenshot()
    sleep(randint(SLEEP_LOWER, SLEEP_UPPER))
