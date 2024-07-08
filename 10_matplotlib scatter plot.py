import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.randn(50)

# x=[10,20,30,40,50]
# y=[10,20,30,40,50]
plt.scatter(x,y,c='red',marker='.',s=100)
plt.show()