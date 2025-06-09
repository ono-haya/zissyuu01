import os
import pandas as pd
path = __path__
df = pd.read_csv(file, encoding='cp932')
df.columns = df.columns.str.strip()
#引数：ranking[[自主専攻のランキング([科目番号, 一致度],[科目番号, 一致度])],[多種専攻のランキング([科目番号, 一致度],[科目番号, 一致度])]]
def get_classinfo(ranking):

    return