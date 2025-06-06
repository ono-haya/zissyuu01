#注：これはコピー
import os
import pandas as pd



def get_credit(file, _major):
    data_path2 = "./all-data" 

    file_path2 = os.path.join(data_path2,"filtered_202310778_courses.csv")
    df = pd.read_csv(file_path2,encoding='cp932')
    class_information = pd.read_csv(file,encoding='cp932')
    # hh = pd.read_csv(os.path.join(data_path,"kdb_2025--ja (1).csv"))

    df.columns = df.columns.str.strip()

    total_credits = df['単位数'].sum()
    #print(f"合計単位数:{total_credits}単位")

    required_major={"システム主専攻","知識科学主専攻","情報資源経営主専攻"}
    major= _major

    if major not in required_major:
        #print("対応していない専攻名です。プログラムを終了します。")
        return [0,0,0,0]
    else:
        if major=="システム主専攻":
            ge7_df = df[df['科目番号'].str.startswith('GE7')]
            geothers_df = df[df['科目番号'].str.startswith(('GE4','GE6','GE8','GA4'))]
            
            target_ge7 = 16
            target_geothers = 8
            #専攻内
            ge7_df_sum = ge7_df['単位数'].sum()
            #専攻外
            geothers_df_sum = geothers_df['単位数'].sum()
            return {target_ge7,ge7_df_sum,target_geothers,geothers_df_sum}
        elif major=="知識科学主専攻":
            ge6_df = df[df['科目番号'].str.startswith('GE6')]
            geothers_df = df[df['科目番号'].str.startswith(('GE4','GE7','GE8','GA4'))]
            
            target_ge6 = 16
            target_geothers = 8
            ge6_df_sum = ge6_df['単位数'].sum()
            geothers_df_sum = geothers_df['単位数'].sum()
            return {target_ge6,ge6_df_sum,target_geothers,geothers_df_sum}
        
        else :
            ge8_df = df[df['科目番号'].str.startswith('GE8')]
            geothers_df = df[df['科目番号'].str.startswith(('GE4','GE6','GE7','GA4'))]

            target_ge8 = 16
            target_geothers = 8
            ge8_df_sum = ge8_df['単位数'].sum()
            geothers_df_sum = geothers_df['単位数'].sum()
            return {target_ge8,ge8_df_sum,target_geothers,geothers_df_sum}


