import os
import pandas as pd


def get_classinfo(rankings):
    csv_path = os.path.join(os.path.dirname(__file__), "kdb.csv")
    df = pd.read_csv(csv_path, encoding='utf-8')
    # クォーテーションや空白を除去して統一
    df["科目番号"] = df["科目番号"].astype(str).str.strip().str.replace('"', '').str.replace("'", "")
    schema = ["科目番号", "科目名", "単位数", "実施学期", "曜時限", "授業概要", "適合度"]
    result = []
    for ranking in rankings:
        array_ranking = [schema.copy()]
        for element in ranking:
            array_element = []
            number = str(element[0]).strip().replace("'", "").replace('"', '').replace(']', '').replace('[', '')
            skip = False
            for label in schema:
                if label == "適合度":
                    array_element.append(f"{element[1]:.2f}")  # 適合度は小数点以下2桁で表示
                else:
                    filtered = df.loc[df['科目番号'] == number, label]
                    if filtered.empty:
                        print(f"該当なし: {number}（label: {label}）")
                        value = None
                    else:
                        value = filtered.iloc[0]
                    # 実施学期がnanならこのデータはスキップ
                    if label == "実施学期" and (pd.isna(value) or value == ""):
                        skip = True
                    array_element.append(value)
            if not skip:
                array_ranking.append(array_element)
        result.append(array_ranking)
    return result