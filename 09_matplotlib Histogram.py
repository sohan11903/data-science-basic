import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 172 , 8
x = mu + sigma * np.random.randn(10000)

plt.hist(x, 100, facecolor ='blue',density=True)
plt.xlabel('heights')
plt.ylabel('percentage of student')
plt.title('heights of student')
plt.grid(True)
plt.text(145,0.04,"u = 172, sig = 8")
plt.show()