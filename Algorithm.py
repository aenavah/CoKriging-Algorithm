import pandas as pd 
import numpy as np


iphone_folder = "/Users/alexandranava/Desktop/DARPA/Exp10/Exp_10_iPhone/"
device_path = "/Users/alexandranava/Desktop/DARPA/Exp10/Exp_10_Device/Exp10_Device_Prob.csv"
iphone_features = ""

iphone_probs = pd.read_csv(iphone_path)
device_probs = pd. read_csv(device_path)
device_features = ""


#assume device is expensive and iphone is cheap 

iphone_probs = iphone_probs[["Image", "Hemostasis", "Inflammation", "Proliferation"]]
device_probs = device_probs[["Image", "Hemostasis", "Inflammation", "Proliferation"]]
#features for both 

pd.concat([iphone_probs, device_probs], axis=0)  # Concatenate DataFrames vertically

def calculate_covariance(V1, V2):
  num_data = len(vector)
  count = 1
  sum = 0 
  while count <= num_data:
    sum += (V1_i - V1^bar)(V2_i-V2^bar)
    count += 1
  cov = sum / num_data
  return cov 

def get_date(string):
  for piece in string:
    if "_" and "0" in piece:
      date_potential = piece.split("-")
      if len(date_potential) == 5:
        #year, month, day, hour, minute
        date = date_potential
        year = date[0]
        month = date[1]
        day = date[2]
        hour = date[3]
        minute = date[4]

        return [year, month, day, hour, minute]
      

if __name__=="__main__":
  #get 
  device_image_link = device_probs["Image"].split("/")
  [year, month, day, hour, minute] = get_date(device_image_link)
  