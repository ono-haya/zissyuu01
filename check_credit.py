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

required_major={"システム主専攻","知識科学主専攻","情報資源経営主専攻"}
major= input("主専攻を入力してください（システム主専攻、知識科学主専攻、情報資源経営主専攻）：")

if major not in required_major:
    print("対応していない専攻名です。プログラムを終了します。")
else:
    if major=="システム主専攻":
        ge7_df = df[df['科目番号'].str.startswith('GE7')&~df['科目番号'].isin(['GE70113','GE70123'])]
        geothers_df = df[df['科目番号'].str.startswith(('GE4','GE6','GE8'))]

        ge7_df_sum = ge7_df['単位数'].sum()
        geothers_df_sum = geothers_df['単位数'].sum()

        if ge7_df_sum > 16:
    
            if geothers_df_sum > 8:
                print('専門科目の単位は足りてる！')

            else:
                lack_credit = 8-geothers_df_sum
                print(f'自分の専攻外の専門科目が{lack_credit}単位足りない')
        else:
            lack_credit7 = 16-ge7_df_sum
            print(f'自分の専攻の専門科目が{lack_credit7}単位足りてないよ')
    elif major=="知識科学主専攻":
        ge6_df = df[df['科目番号'].str.startswith('GE6')&~df['科目番号'].isin(['GE60113','GE60123'])]
        geothers_df = df[df['科目番号'].str.startswith(('GE4','GE7','GE8'))]

        ge6_df_sum = ge6_df['単位数'].sum()
        geothers_df_sum = geothers_df['単位数'].sum()

        if ge6_df_sum > 16:
    
            if geothers_df_sum > 8:
                print('専門科目の単位は足りてる！')

            else:
                lack_credit = 8-geothers_df_sum
                print(f'自分の専攻外の専門科目が{lack_credit}単位足りない')
        else:
            lack_credit6 = 16-ge6_df_sum
            print(f'自分の専攻の専門科目が{lack_credit6}単位足りてないよ')
    else :
        ge8_df = df[df['科目番号'].str.startswith('GE8')&~df['科目番号'].isin(['GE80113','GE80123'])]
        geothers_df = df[df['科目番号'].str.startswith(('GE4','GE6','GE7'))]

        ge8_df_sum = ge8_df['単位数'].sum()
        geothers_df_sum = geothers_df['単位数'].sum()

        if ge8_df_sum > 16:
    
            if geothers_df_sum > 8:
                print('専門科目の単位は足りてる！')

            else:
                lack_credit = 8-geothers_df_sum
                print(f'自分の専攻外の専門科目が{lack_credit}単位足りない')
        else:
            lack_credit8 = 16-ge8_df_sum
            print(f'自分の専攻の専門科目が{lack_credit8}単位足りてないよ')

    

