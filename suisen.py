import os
import pandas as pd

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


n = 0
gacchi = []
v = 0
pro = []

for samp in "system_sample_data":
    for cls in samp:
        if cls in df['科目番号']:
            n += 1
    gacchi.append(n / len(samp))

for i in "tenchi_system":
    if i[0] not in df['科目番号']:
        for j in "tenchi_system"[1]:
            v += gacchi[j]
        gacchiritu = v / len("tenchi_system"[1])
        pro.append([i[0] , gacchiritu])


sorted_data = sorted(pro, key=lambda x: x[1], reverse=True)