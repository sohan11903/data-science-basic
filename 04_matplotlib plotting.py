import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100,101,1)
y1 = 0.5 * x ** 2 + 2 * x
y = np.sin(x)*2000
y2 = np.log(x)*1000
y3 =np.log(x)*-1000

plt.plot(x, y , 'r--')  #'ro' 'g' 'y' 
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()