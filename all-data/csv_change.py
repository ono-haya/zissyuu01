
import pandas as pd

# CSVファイルを読み込み
df = pd.read_csv(r"C:\Users\be_ke\zissyuu01\zissyuu01\all-data\kdb_2025--ja (1).csv", encoding="utf-8-sig")

# 「科目番号」列が GE4, GE6, GE7, GE8 で始まる行だけ抽出かつ科目番号、科目名、単位数だけ抽出
filtered_df = df[df["科目番号"].astype(str).str.startswith(("GE4", "GE6", "GE7", "GE8"))]
simple_df = filtered_df[["科目番号","科目名","単位数"]]
# 結果を新しいCSVとして保存
simple_df.to_csv("filtered_ge_courses.csv", index=False, encoding="cp932")
