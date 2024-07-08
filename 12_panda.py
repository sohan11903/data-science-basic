import pandas as pd
import matplotlib.pyplot as plt

# series = pd.Series([10,20,30,40],['A','B','C','D'])
# print(series)
# A    10
# B    20
# C    30
# D    40
# print(series['C'])  #30  if 10 => A
# print(series.iloc[2]) #30
# series.name = "mySeries"
# print(dict(series))  #convert in dict

s1 = pd.Series([1,2,3,4],['A','B','C','D'])
s2 = pd.Series([12,21,34,41],['A','B','C','D'])
# print(s1 + s2)
# A    13
# B    23
# C    37
# D    45
# print(s1.count())
print(s1.head(2))
print(s1.tail(2))

def mysq(x):
    return x ** 2

print(s1.apply(mysq))
print(s2.sort_index)
print(s2.sort_values(inplace=True))

# s1.plot() #graph
# s1.plot.bar() #block || 
# s1.plot.pie() 
# plt.show()

s1.to_csv('myseries.csv')