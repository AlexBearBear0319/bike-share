import os
import pandas as pd # pip install pandas

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = master_df.append(pd.read_csv(file))


master_df.to_csv('Master File TESLA.csv', index=False)
