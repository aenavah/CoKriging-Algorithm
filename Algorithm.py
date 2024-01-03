import pandas as pd 
import numpy as np


iphone_path = "/Users/alexandranava/Desktop/DARPA/Exp10/Exp_10_iPhone/Exp10_iPhone_probtable_V8.csv"
device_path = "/Users/alexandranava/Desktop/DARPA/Exp10/Exp_10_Device/Exp10_Device_Prob.csv"

iphone_probs = pd.read_csv(iphone_path)
device_probs = pd. read_csv(device_path)

#assume device is expensive and iphone is cheap 

iphone_probs = iphone_probs[["Hemostasis", "Inflammation", "Proliferation"]]
device_probs = device_probs[["Hemostasis", "Inflammation", "Proliferation"]]

pd.concat([iphone_probs, device_probs], axis=0)  # Concatenate DataFrames vertically
