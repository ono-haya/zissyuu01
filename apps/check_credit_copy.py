#注：これはコピー
import os
import pandas as pd



def get_credit(file, _major):
    data_path2 = os.path.join(os.path.dirname(__file__), "..", "all-data")
    file_path2 = os.path.join(data_path2, "filtered_ge_courses.csv")
    df = pd.read_csv(file_path2, encoding='cp932')
    class_information = pd.read_csv(file, encoding='cp932')

    df.columns = df.columns.str.strip()

    required_major = {"システム主専攻", "知識科学主専攻", "情報資源経営主専攻"}
    major = _major

    # デフォルト値
    result = {
        "target": 0,
        "main_sum": 0,
        "other_target": 0,
        "other_sum": 0
    }

    if major == "システム主専攻":
        ge_main = df[df['科目番号'].str.startswith('GE7')]
        ge_others = df[df['科目番号'].str.startswith(('GE4', 'GE6', 'GE8', 'GA4'))]
        result["target"] = 16
        result["main_sum"] = int(ge_main['単位数'].sum())
        result["other_target"] = 8
        result["other_sum"] = int(ge_others['単位数'].sum())
    elif major == "知識科学主専攻":
        ge_main = df[df['科目番号'].str.startswith('GE6')]
        ge_others = df[df['科目番号'].str.startswith(('GE4', 'GE7', 'GE8', 'GA4'))]
        result["target"] = 16
        result["main_sum"] = int(ge_main['単位数'].sum())
        result["other_target"] = 8
        result["other_sum"] = int(ge_others['単位数'].sum())
    elif major == "情報資源経営主専攻":
        ge_main = df[df['科目番号'].str.startswith('GE8')]
        ge_others = df[df['科目番号'].str.startswith(('GE4', 'GE6', 'GE7', 'GA4'))]
        result["target"] = 16
        result["main_sum"] = int(ge_main['単位数'].sum())
        result["other_target"] = 8
        result["other_sum"] = int(ge_others['単位数'].sum())
    # majorが該当しない場合はデフォルト値のまま

    return result


