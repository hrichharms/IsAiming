import tkinter as tk
import os
import json

data = os.listdir("Data/FILTERED")

labels = json.load(open("labels.json"))
already_done = [i[1] for i in labels]
print(len(already_done), "already labeled.")

i = 0
while data[i] in already_done: i += 1

root = tk.Tk()
img = tk.PhotoImage(file="Data/FILTERED/" + data[i])
label = tk.Label(root, image=img)
label.pack()

def callback(e):
    global data, i, labels
    valid = False
    if e.char == "w" or e.char == "s":
        valid = True
        labels.append([(e.char == "w") * 1, data[i]])
    elif e.char == "q":
        json.dump(labels, open("labels.json", "w"))
    if valid:
        i += 1
        img = tk.PhotoImage(file="Data/FILTERED/" + data[i])
        label.config(image=img)
        label.image = img

root.bind("<Key>", callback)
root.mainloop()
