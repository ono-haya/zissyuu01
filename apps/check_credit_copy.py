def get_credit(file, _major):
    import os
    import pandas as pd

    df = pd.read_csv(file, encoding='cp932')
    df.columns = df.columns.str.strip()
    major = _major

    # 除外科目の辞書
    exclude_codes = {
        "システム主専攻": ['GE70113', 'GE70123'],
        "知識科学主専攻": ['GE60113', 'GE60123'],
        "情報資源経営主専攻": ['GE80113', 'GE80123']
    }
    # 主専攻ごとのprefix
    main_prefix = {
        "システム主専攻": 'GE7',
        "知識科学主専攻": 'GE6',
        "情報資源経営主専攻": 'GE8'
    }
    # 他専攻prefix
    other_prefix = {
        "システム主専攻": ('GE4', 'GE6', 'GE8', 'GA4'),
        "知識科学主専攻": ('GE4', 'GE7', 'GE8', 'GA4'),
        "情報資源経営主専攻": ('GE4', 'GE6', 'GE7', 'GA4')
    }

    result_state = {
        "target": 0,
        "main_sum": 0,
        "other_target": 0,
        "other_sum": 0
    }

    if major in main_prefix:
        ge_main = df[df['科目番号'].str.startswith(main_prefix[major]) & ~df['科目番号'].isin(exclude_codes[major])]
        ge_others = df[df['科目番号'].str.startswith(other_prefix[major])]
        result_state["target"] = 16
        result_state["main_sum"] = int(ge_main['単位数'].sum())
        result_state["other_target"] = 8
        result_state["other_sum"] = int(ge_others['単位数'].sum())
    # majorが該当しない場合はデフォルト値のまま
    return [result_state, main_prefix[major], other_prefix[major]]