import os
import pandas as pd

data_path = "./data"

df = pd.read_csv(os.path.join(data_path,"filtered_202310778_courses.csv"))
class_information = pd.read_csv(os.path.join(data_path,"filtered_ge_courses.csv"))
# hh = pd.read_csv(os.path.join(data_path,"kdb_2025--ja (1).csv"))
df.columns = df.columns.str.strip()


big_file = []

for i in df_transposed:
    big_file.append([])
    for j in df_transposed[i]:
        big_file[i].append(j)

print(big_file)
