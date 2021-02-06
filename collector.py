from PIL import ImageGrab
from random import randint
from time import sleep
from socket import gethostname
from datetime import datetime
import win32api
import threading
from hashlib import sha1
from os import mkdir
from os import getcwd

SLEEP_LOWER, SLEEP_UPPER = [3, 3]
WIDTH, HEIGHT = ImageGrab.grab().size
HOSTNAME = gethostname()

def screenshot(session_dir):
    im = ImageGrab.grab(bbox=(WIDTH // 2 - 50, HEIGHT // 2 - 50, WIDTH // 2 + 50, HEIGHT // 2 + 50))
    time_component = str(datetime.now()).split(".")[0].replace(":", "")
    im.save("Data/" + session_dir + "/" + HOSTNAME.replace("-", "") + "_" + time_component + ".png")

class Mouse_thread(threading.Thread):

    def __init__(self, session_dir):
        threading.Thread.__init__(self)
        self.running = False
        self.session_dir = session_dir
    
    def run(self):
        self.running = True
        state_left = win32api.GetKeyState(0x01)
        while self.running:
            a = win32api.GetKeyState(0x01)
            if a != state_left:
                state_left = a
                if a < 0:
                    screenshot(self.session_dir)
            sleep(0.1)

if __name__ == "__main__":

    session_dir = HOSTNAME + "_" + sha1(str(randint(1, 1e32)).encode()).hexdigest()[:13]
    mkdir("Data/" + session_dir)

    t = Mouse_thread(session_dir)
    t.start()

    try:
        while True:
            screenshot(session_dir)
            sleep(randint(SLEEP_LOWER, SLEEP_UPPER))
    except KeyboardInterrupt: pass

    t.running = False
    t.join()
