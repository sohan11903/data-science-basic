import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('dark_background')
x = np.arange(0,30,0.2)
y1 = np.sin(x)
y2 = np.cos(x)

# plt.grid(True)
# plt.title("sin function") #mid
plt.suptitle("sin function")  #top
plt.xlabel("number of student")
plt.ylabel("heigth of student")
plt.plot(x,y1 , label = "sin")
plt.plot(x,y2 , label = "cos")
plt.legend(loc = "lower right")
plt.show()