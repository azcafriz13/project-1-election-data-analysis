import pandas as pd
import matplotlib
from prophet import Prophet
import datetime
import sys
import openpyxl

file_name = "1976-2020-president.csv"
file = file_name
res = 1
df = pd.read_csv(file)
df = df.reset_index(drop = True)
df = df[df['year'] != 2020]

for i in df.index:
  if (df.loc[i, 'party_simplified'] != "REPUBLICAN") and (df.loc[i, 'party_simplified'] != "DEMOCRAT"):
    df.loc[i, 'party_simplified'] = 'OTHER'
df = df.reset_index(drop=True)

start_date = datetime.datetime(1976,11,5)
end_date = datetime.datetime(2016,11,5)
delta = datetime.timedelta(days=((365*4)+1))
year_list = []
while start_date <= end_date:
    year_list.append(start_date)
    start_date += delta

party_list = ['DEMOCRAT', 'REPUBLICAN', 'OTHER']
state_list = df['state'].unique()
df1 = pd.DataFrame()
i=0

for year in year_list:
    for state in state_list:
        df1.loc[i,'year'] = year.year
        df1.loc[i,'state'] = state
        for party in party_list:
            temp = df.loc[(df['state'] == state) & (df['year'] == year.year) &
                          (df['party_simplified'] == party), 'candidatevotes'].sum()
            if party == 'DEMOCRAT':
                df1.loc[i,'democrat'] = temp
            if party == 'REPUBLICAN':
                df1.loc[i,'republican'] = temp
            if party == 'OTHER':
                df1.loc[i,'other'] = temp
        i+=1

df=df1
del df1

keys = []
val = []
for state in state_list:
    keys.append(state)
    df1 = df[df['state'] == state]
    val.append(df1)

del df1
party_list = [x.lower() for x in party_list]

dict_results = dict(zip(keys, val))
df1 = pd.DataFrame()
final_values = []
for key, values in dict_results.items():
    temp = []
    for party in party_list:
        if party == 'democrat':
            df1 = pd.DataFrame({'ds': year_list, 'y': values.democrat})
        if party == 'republican':
            df1 = pd.DataFrame({'ds': year_list, 'y': values.republican})
        if party == 'other':
            df1 = pd.DataFrame({'ds': year_list, 'y': values.other})
        df1 = df1.reset_index()
        m = Prophet()
        m.fit(df1)
        future = m.make_future_dataframe(periods=1)
        forecast = m.predict(future)
        forecast.loc[11,'ds'] = datetime.datetime(2020,11,5)
        temp.append(forecast)
        del df1
        del forecast
        del m
        del future
    final_values.append(temp)
    del temp

dict_final_results = dict(zip(keys, final_values))

output_table = pd.DataFrame()
j=0
for key, value in dict_final_results.items():
    output_table.loc[j,'State'] = key
    k=0
    for items in value:
        i = len(items)-1
        output_table.loc[j,party_list[k]] = int(items['yhat'][i])
        k+=1
    j+=1

df=output_table
del output_table

len = df.shape[0]
len1 = df.shape[1]

for i in range(0,len):
    total = 0
    for j in range(1,len1):
        total = df.iloc[i,j] + total
    df.loc[i,'Total Votes'] = total

for i in range(0,len):
    df.loc[i, 'Winner'] = "Other"
    if (df.iloc[i,1] > df.iloc[i,2]) and (df.iloc[i,1] > df.iloc[i,3]):
        df.loc[i,'Winner'] = "Democrat"
    if (df.iloc[i, 2] > df.iloc[i, 1]) and (df.iloc[i, 2] > df.iloc[i, 3]):
        df.loc[i, 'Winner'] = "Republican"

df.to_excel("2020 results by state.xlsx")
del df



















