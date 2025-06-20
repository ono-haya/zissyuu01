import os
import pandas as pd

# データ読み込み
data_path2 = "./all-data" 
file_path1 = os.path.join(data_path2,"filtered_ge_courses.csv")
file_path2 = os.path.join(data_path2,"filtered_202310778_courses.csv")

df = pd.read_csv(file_path2, encoding='cp932')
class_information = pd.read_csv(file_path1, encoding='cp932')
df.columns = df.columns.str.strip()

# 合計単位数
total_credits = df['単位数'].sum()
print(f"合計単位数:{total_credits}単位")

# 対象データ
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

# 科目番号を文字列リスト化
yy = df["科目番号"].astype(str).tolist()


gacchi = []  # 各サンプルの履修率を保存するリスト

for samp in system_sample_data:  # 各サンプルについて処理する
    count = 0  # 履修済み（yyに含まれている）科目の数をカウントする変数

    for cls in samp:  # サンプル内の各クラスを1つずつ確認
        if cls in yy:  # そのクラスが履修済みであれば
            count += 1  # カウントを1増やす

    total = len(samp)  # サンプル内の総クラス数
    rate = count / total  # 履修率（= 該当数 / 総数）を計算
    gacchi.append(rate)  # 結果リストに履修率を追加

# 未履修科目に対して推薦度計算
pro = []
for i in tenchi_system:
    if i[0][0] not in yy:
        v = sum(gacchi[j] for j in i[1])
        gacchiritu = v / len(i[1])
        pro.append([i[0], gacchiritu])

# 推薦度でソート
sorted_data = sorted(pro, key=lambda x: x[1], reverse=True)
match_result = sorted_data[:3]
# 結果出力

for item in match_result:
    subject = item[0][0]
    score = item[1]
    score_int = int(score*100)
    print(f"[{subject}, {score_int}]")

    
