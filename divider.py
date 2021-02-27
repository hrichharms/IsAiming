import os
import shutil
import json

labels = {i[1]: i[0] for i in json.load(open("labels.json"))}

cwd = os.getcwd()
processed = [i for i in os.listdir("Data/PROCESSED")]
n = len(processed)

training_portion = float(input("Portion of data to use for training (0-1): "))

training_examples = int(n * training_portion)

training, testing = processed[:training_examples], processed[training_examples:]

for example in training: shutil.copyfile(cwd + "/Data/PROCESSED/" + example, cwd + "/Data/TRAINING/" + str(labels[example]) + "/" + example)
for example in testing: shutil.copyfile(cwd + "/Data/PROCESSED/" + example, cwd + "/Data/TESTING/" + str(labels[example]) + "/" + example)
