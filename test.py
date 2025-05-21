import os
import pandas as pd

data_path = "./data"

df = pd.read_csv(os.path.join(data_path,"SIR202312990 (4).csv"))

print(df)