import pandas as pd

### Reading different data files
poke_csv = pd.read_csv('pokemon_data.csv')
# print(poke_csv.tail(5))

poke_xlsx = pd.read_excel('pokemon_data.xlsx')
# Requires openpyxl package
# print(poke_xlsx.tail(5))

poke_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')
# Delimiter needed to replace escape sequence with proper visual representation for txt
print(poke_txt.tail(5))

### Reading Data

## Read Headers
print(poke_csv.columns)

## Read each Column
print(poke_csv['Name'][0:5]) # One Header
print(poke_csv[['Name', 'Type 1', 'HP']]) # Multiple Headers

## Read each Row
print(poke_csv.iloc[1]) # Integer location of record, i.e. record[1]
print(poke_csv.iloc[1:4]) # Multiple Integer locations i.e. record 1-4
for index, row in poke_csv.iterrows():
  print(index, row)

## Read a specific location
print(poke_csv.iloc[2,1])
