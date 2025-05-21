import os
import pandas as pd

data_path = "./data"

df = pd.read_csv(os.path.join(data_path,"SIRS202312990 (4).csv"))

hh = pd.read_csv(os.path.join(data_path,"kdb_2025--ja (1).csv"))

print(hh)

#for i in df:
 #   for n in df[i]:
  #      if n == "情報メディア入門":
   #         print(n)
    # print(df[i])