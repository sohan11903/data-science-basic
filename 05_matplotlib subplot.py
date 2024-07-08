import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,101,1)
# y1 = 0.5 * x ** 2 + 2 * x
y = np.sin(x)
y2 = x ** 2 + 2 *x 

# ax1 = plt.subplot(221) 
# ax2 = plt.subplot(222) 
# ax3 = plt.subplot(223) 
# ax4 = plt.subplot(224) 
 
# ax1.plot(x, y)
# ax2.plot(x, y2)
# ax3.plot(x, y2 , 'r')
# ax4.plot(x, y2 , 'g')

# plt.tight_layout()
# plt.show()


plt.figure(1) #multiple windows
ax1 = plt.subplot(211)
ax1.plot(x,y, 'g')

ax2 = plt.subplot(212)
ax2.plot(x,y2,'y')

plt.figure(2)
plt.plot(x,y, 'g')

plt.figure(3)
plt.plot(x,y2,'r')


plt.show()