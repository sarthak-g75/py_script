import pickle
import sys
import numpy as np
import pandas as pd
import json


print("hello world")

with open('model', 'rb') as f:
    mp = pickle.load(f)

arr = []
for i in range(len(sys.argv)):
    if i == 0: continue;
    arr.append(float(sys.argv[i]))
    
# Data to be written
dictionary = {
    "charge": mp.predict([[float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]),
                           float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]),
                           float(sys.argv[7]), float(sys.argv[8]),float(sys.argv[9]),
                           float(sys.argv[10]), float(sys.argv[11])]])[0]
}


json_object = json.dumps(dictionary, indent=4)

with open("charges.json", "w") as outfile:
    outfile.write(json_object)
