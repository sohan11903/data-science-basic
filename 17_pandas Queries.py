import pandas as pd

df = pd.read_csv('people.csv',delimiter=',')
df.set_index('SSN',inplace=True)
print(df)
result = df.loc[(df['Age'] > 45) & (df['Height'] > 149)]['Name']
print(result)
