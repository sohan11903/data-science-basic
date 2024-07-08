import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection = "3d")
# z = np.linspace(0,30,100)
# x= np.sin(z)
# y = np.cos(z)
def z_function(x,y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
x,y = np.meshgrid(x,y)
z = z_function(x,y)
ax.plot_surface(x,y,z)
plt.show()