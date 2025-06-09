import os
import pandas as pd
import json

data_path1 = "./data"
data_path2 = "./all-data" 

file_path1 = os.path.join(data_path2,"filtered_ge_courses.csv")
file_path2 = os.path.join(data_path2,"filtered_202310778_courses.csv")
df = pd.read_csv(file_path2,encoding='cp932')
class_information = pd.read_csv(file_path1,encoding='cp932')
# hh = pd.read_csv(os.path.join(data_path,"kdb_2025--ja (1).csv"))

df.columns = df.columns.str.strip()


total_credits = df['単位数'].sum()
print(f"合計単位数:{total_credits}単位")

######################################################################



system_sample_data = [
    ["GE60601", "GE60801", "GE61101", "GE70301", "GE70401", "GE73201", "GE70501", "GE70601", "GE70701", "GE71001", "GE72501", "GE72801", "GE80501", "GE82601"],
    ["GE61101", "GE61801", "GE61901", "GE70201", "GE70401", "GE70601", "GE71001", "GE71101", "GE72801", "GE82601", "GE80801", "GE80901", "GE81101", "GE81301", "GE40401"],
    ["GE61101", "GE61801", "GE61901", "GE62001", "GE70201", "GE70301", "GE70401", "GE73201", "GE70501", "GE70701", "GE70801", "GE71001", "GE71101", "GE72801", "GE71901", "GE81201", "GE40401"],
    ["GE60201", "GE61101", "GE62301", "GE70301", "GE73201", "GE70501", "GE70601", "GE70701", "GE71101", "GE72501", "GE72601", "GE72801", "GE71901", "GA40503", "GA40603"],
    ["GE73201", "GE70501", "GE70701", "GE72601", "GE72801", "GE71901", "GA40103", "GA40203", "GA40503", "GA40603"],
    ["GE62601", "GE61801", "GE62401", "GE70601", "GE70701", "GE72701", "GE70801", "GE70901", "GE71001", "GE71101", "GE72601", "GE72801", "GE71801", "GE80301", "GE80501", "GE80901"],
    ["GE61101", "GE61801", "GE70201", "GE70301", "GE70501", "GE70601", "GE70701", "GE70801", "GE70901", "GE71001", "GE72801", "GE80901", "GE81401", "GA40603", "GA40803", "GE40501"],
    ["GE61101", "GE70301", "GE70401", "GE70501", "GE70701", "GE70801", "GE71001", "GE72801", "GE40201", "GE40301", "GE40401", "GE40501"],
    ["GE60601", "GE61801", "GE61901", "GE70201", "GE70401", "GE73201", "GE70501", "GE70701", "GE71001", "GE71901", "GE81301", "GE40201", "GE40401"],
    ["GE60601", "GE70201", "GE70301", "GE70401", "GE70501", "GE70601", "GE71001", "GE71901", "GE81201", "GE40201", "GE40401", "GE40501"]
    ]

tenchi_system = [
    [['GE40201'], [0, 1, 2, 3]],
    [['GE40301'], [0, 1, 2, 3, 4]],
    [['GE40401'], [0, 1, 2, 3, 4]],
    [['GE40501'], [2, 3]],
    [['GE40603'], [0, 1, 2, 3, 4]],
    [['GE40703'], [0]],
    [['GE60201'], [0, 1, 2, 3, 4]],
    [['GE60501'], [2]],
    [['GE60601'], [0, 1, 2, 3]],
    [['GE60801'], [4]],
    [['GE61101'], [0, 1, 2, 3]],
    [['GE62201'], [1]],
    [['GE62601'], [3]],
    [['GE62701'], [2]],
    [['GE70401'], [0]],
    [['GE70501'], [3, 4]],
    [['GE70601'], [3, 4]],
    [['GE70701'], [3]],
    [['GE70801'], [3]],
    [['GE72601'], [3]],
    [['GE73201'], [0]],
    [['GE80301'], [0, 1, 2, 4]],
    [['GE80501'], [0, 1, 2, 3, 4]],
    [['GE80801'], [0, 1, 2, 4]],
    [['GE80901'], [0, 1, 2, 3, 4]],
    [['GE81101'], [0, 1, 2, 3]],
    [['GE81201'], [0, 1, 2, 3, 4]],
    [['GE81301'], [1, 2, 3, 4]],
    [['GE81401'], [1, 3, 4]],
    [['GE82601'], [0, 1, 2, 4]],
    [['GE82802'], [0, 1]],
    [['GE82901'], [0, 1, 2, 4]],
    [['GE83001'], [1, 4]]
]

 ##

n = 0
gacchi = []
pro = []


yy = df["科目番号"].astype(str).tolist()




for samp in system_sample_data:
    n = 0
    for cls in samp:
        if cls in yy:
            n += 1
    print(n)
    gacchi.append(n / len(samp))

for i in tenchi_system:
    if i[0][0] not in yy:
        v = 0
        for j in i[1]:
            v += gacchi[j]
        gacchiritu = v / len(tenchi_system[1])
        pro.append([i[0] , gacchiritu])


sorted_data = sorted(pro, key=lambda x: x[1], reverse=True)

print(sorted_data)
