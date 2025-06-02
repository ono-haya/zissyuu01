import os
import pandas as pd


data_path = "./data"

data_name = "data"

data_list = os.listdir(data_name)

count_class = []
x = 0

for i in data_list:
    df = pd.read_csv(os.path.join(data_path,i))
    df_transposed = df.T
    big_file = []
    for z in df_transposed:
        big_file.append([])
        for j in df_transposed[z]:
            big_file[z].append(j)
    
    for t in big_file:
        if t[3] == "図書館概論":
            x += 1
print(x)