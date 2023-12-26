#%%
import json
import pandas as pd
import calendar
import numpy as np
import datetime as dt

#%%
df = pd.read_csv("carga_historica_DN_1.txt", sep='\t', encoding='utf-8', header=None, skiprows=1, comment='#')
df.rename(columns={0: 'datetime'}, inplace=True)

# %%
df['datetime'] = pd.to_datetime(df['datetime'], infer_datetime_format=True)
df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
print(df.head(15))
#%%
df1 = pd.melt(df, id_vars=['datetime'], value_vars=df.columns[2:], var_name='Id_row', value_name='value')
print(df1.head(15))
# %%
