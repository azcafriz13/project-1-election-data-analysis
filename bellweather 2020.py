import pandas as pd
import matplotlib
from prophet import Prophet
import datetime
import sys
import openpyxl

list_of_dataframes = []
file = "Book1.xlsx"
wb = openpyxl.load_workbook(file)
res = len(wb.sheetnames)

# read in the election results for each county
for i in range(1,res+1):
    df = pd.read_excel(file, sheet_name='Sheet'+str(i))
    df['Year'] = pd.to_datetime(df['Year'].astype(str)) + datetime.timedelta(days=+309)
    df = df.loc[df['Year'].dt.year < 2016]
    df = df.loc[df['Year'].dt.year > 1976]
    df.reset_index(inplace=True)
    df['Total Votes'] = df.sum(axis=1, numeric_only=True)
    list_of_dataframes.append(df)

keys = []
val = []
for items in list_of_dataframes:
    keys.append(items['County'][0])
    forecast_list = []
    for name, values in items.items():
        if name == 'Republican' or name == 'Democratic' or name == 'Other':
            df1 = pd.DataFrame({'ds': items['Year'],'y': values})
            m = Prophet()
            m.fit(df1)
            future = m.make_future_dataframe(periods=1)
            forecast = m.predict(future)
            forecast_list.append(forecast)
            del forecast
            del future
            del df1
            del m
    val.append(forecast_list)
    del forecast_list

dict_results = dict(zip(keys, val))
del keys
del val

output_table = pd.DataFrame()
j=0
party_list = ['Republican', 'Democratic', 'Other']
for key, value in dict_results.items():
    output_table.loc[j,'County'] = key
    k=0
    for items in value:
        i = len(items)-1
        output_table.loc[j,party_list[k]] = int(items['yhat'][i])
        k+=1
    j+=1

df = output_table
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
        df.loc[i,'Winner'] = "Republican"
    if (df.iloc[i, 2] > df.iloc[i, 1]) and (df.iloc[i, 2] > df.iloc[i, 3]):
        df.loc[i, 'Winner'] = "Democratic"

df.to_excel("bellweather 2020 output.xlsx")
del df
