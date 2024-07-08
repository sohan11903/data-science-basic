import numpy as np
import matplotlib.pyplot as plt

python = (85,67,23,98)
java = (50,67,89,14)
networking = (60,20,56,22)
machine_learning = (88,23,40,87)

people = ['bob','anna','john','mark']
index = np.arange(4)
plt.bar(index, python , width=0.2 , label  = "Python")
plt.bar(index + 0.2, java , width=0.2 , label  = "java")
plt.bar(index + 0.4, networking , width=0.2 , label  = "networking")
plt.bar(index + 0.6, machine_learning , width=0.2 , label  = "machine learning")
plt.title("IT skill level")
plt.xlabel("person")
plt.ylabel("skill level")
plt.xticks(index + 0.2 , people)
plt.legend(loc = "upper left")
plt.ylim(0,120)
plt.show()