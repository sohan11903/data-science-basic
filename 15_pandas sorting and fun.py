import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data ={
    'SSN' : [123,445,511,872,348],
    'Name' : ['sohan','anna','mike','john','abc'],
    'Age' : [20,23,26,29,32],
    'height' : [176,165,107,179,123],
    'Gender' : ['m', 'f' ,'m','m','m']
    
}
df = pd.DataFrame(data)
df.set_index('SSN',inplace=True)
# print(df['height'].apply(np.sin))
# print(df['height'].apply(lambda x:x*100))

# for key,value in df['height'].iteritems():
#     print("{}: {}".format(key,value))

df.sort_index(inplace=True)
print(df)
df.sort_values(by=['Name','Age'],inplace=True)
print(df)
