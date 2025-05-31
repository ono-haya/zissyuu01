
import pandas as pd

try: 
# CSVファイルを読み込み
    df = pd.read_csv(r"../data/SIRS202310778 (2).csv", encoding="utf-8-sig")
except FileNotFoundError:
    print("ファイルが見つかりません")
except Exception as e:
    print(f"ファイルの読み込み中に予期しないエラーが発生した:{e}")
else:
    try:

# 「科目番号」列が GE4, GE6, GE7, GE8 で始まる行だけ抽出かつ科目番号、科目名、単位数だけ抽出
        filtered_df = df[df["科目番号"].astype(str).str.startswith(("GE4", "GE6", "GE7", "GE8"))]
     

        simple_df = filtered_df[["科目番号","科目名 ","単位数"]]
# 結果を新しいCSVとして保存
        simple_df.to_csv("filtered_202310778_courses.csv", index=False, encoding="cp932")
    except Exception as e:
        print(f"データ処理中にエラーが発生しました:{e}")
