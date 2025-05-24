import os
import pandas as pd

data_path = "./data"

df = pd.read_csv(os.path.join(data_path,"SIRS202312990 (4).csv"))

# hh = pd.read_csv(os.path.join(data_path,"kdb_2025--ja (1).csv"))

df_transposed = df.T

big_file = []

for i in df_transposed:
    big_file.append([])
    for j in df_transposed[i]:
        big_file[i].append(j)

x = []

for i in big_file:
    if i[7] == "履修中":
        x.append(i[3])

print(x)
