import os
import pandas as pd
path = __path__


#引数：ranking[[自主専攻のランキング([科目番号, 一致度],[科目番号, 一致度])],[多種専攻のランキング([科目番号, 一致度],[科目番号, 一致度])]]
def get_classinfo(rankings):
    df = pd.read_csv("./kdb.csv", encoding='cp932')
    df.columns = df.columns.str.strip()
    schema = ["科目番号","科目名","単位数","実施学期","曜時限","授業概要"]
    result = [[]]
    for ranking in rankings:
        for element in ranking:
            number = element[0]
            osusume = element[1]
            element_info = df[df["科目番号"] == number]
            
            

    return