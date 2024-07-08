import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names ={
    'SSN' : [2,5,7,8],
    'name' :['sohan','smit','mitul','xyz']
}

ages ={
    'SSN' : [1,2,3,5],
    'name' :[28,34,45,62]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

# df = pd.merge(df1,df2, on='SSN' ,how='outer')
# df = pd.merge(df1,df2, on='SSN' ,how='inner')
# df = pd.merge(df1,df2, on='SSN' ,how='left')
df = pd.merge(df1,df2, on='SSN' ,how='right')
df.set_index('SSN',inplace=True)
print(df)