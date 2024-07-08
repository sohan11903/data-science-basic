import pandas as pd
import matplotlib.pyplot as plt

data ={
    'SSN' : [123,445,511,872],
    'Name' : ['sohan','anna','mike','john'],
    'Age' : [20,23,26,29],
    'height' : [176,165,107,179],
    'Gender' : ['m', 'f' ,'m','m']
    
}
df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)
print(df)
# SSN   Name  Age  height Gender
# 
# 123  sohan   20     176      m
# 445   anna   23     165      f
# 511   mike   24     107      m
# 872   john   23     179      m
# print(df.head(3))
# print(df.tail(3))
# print(df.ndim)
# print(df.shape)
# print(df.size)
# print(df.dtypes)
# print(df.T)
# print(df['Name'].iloc[1])
# print(df.iloc[0:2])
# df.hist()
# df.plot.bar()
df.Age.hist()
plt.show()