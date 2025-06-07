def get_credit(file, _major):
    import os
    import pandas as pd

    df = pd.read_csv(file, encoding='cp932')

    df.columns = df.columns.str.strip()

    major = _major

    # デフォルト値
    result = {
        "target": 0,
        "main_sum": 0,
        "other_target": 0,
        "other_sum": 0
    }

    if major == "システム主専攻":
        # GE70113, GE70123を除外
        ge_main = df[df['科目番号'].str.startswith('GE7') & ~df['科目番号'].isin(['GE70113', 'GE70123'])]
        ge_others = df[df['科目番号'].str.startswith(('GE4', 'GE6', 'GE8', 'GA4'))]
        result["target"] = 16
        result["main_sum"] = int(ge_main['単位数'].sum())
        result["other_target"] = 8
        result["other_sum"] = int(ge_others['単位数'].sum())
    elif major == "知識科学主専攻":
        # GE60113, GE60123を除外
        ge_main = df[df['科目番号'].str.startswith('GE6') & ~df['科目番号'].isin(['GE60113', 'GE60123'])]
        ge_others = df[df['科目番号'].str.startswith(('GE4', 'GE7', 'GE8', 'GA4'))]
        result["target"] = 16
        result["main_sum"] = int(ge_main['単位数'].sum())
        result["other_target"] = 8
        result["other_sum"] = int(ge_others['単位数'].sum())
    elif major == "情報資源経営主専攻":
        # GE80113, GE80123を除外
        ge_main = df[df['科目番号'].str.startswith('GE8') & ~df['科目番号'].isin(['GE80113', 'GE80123'])]
        ge_others = df[df['科目番号'].str.startswith(('GE4', 'GE6', 'GE7', 'GA4'))]
        result["target"] = 16
        result["main_sum"] = int(ge_main['単位数'].sum())
        result["other_target"] = 8
        result["other_sum"] = int(ge_others['単位数'].sum())
    # majorが該当しない場合はデフォルト値のまま

    return result