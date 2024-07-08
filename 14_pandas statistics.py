import pandas as pd
import matplotlib.pyplot as plt

data ={
    'SSN' : [123,445,511,872,348],
    'Name' : ['sohan','anna','mike','john','abc'],
    'Age' : [20,23,26,29,32],
    'height' : [176,165,107,179,123],
    'Gender' : ['m', 'f' ,'m','m','m']
    
}
df= pd.DataFrame(data)
df.set_index('SSN')
# print(df.count())
# print(df['Age'].count())
# print(df['Age'].sum())  #prod
print(df['height'].mean())
print(df['height'].median())
print(df['height'].mode())
print(df['height'].std().__round__())
print(df['height'].min())
print(df['height'].max())
print(df['height'].describe())
