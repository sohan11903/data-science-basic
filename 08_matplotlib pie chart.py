import matplotlib.pyplot as plt

nationalities = ['American' , 'German' , 'Indian' , 'Other']
student = [60,23,21,34]
color = ['blue','red','yellow' , 'pink']
plt.pie(student,labels=nationalities, autopct='%.2f%%',counterclock=False,startangle=90,colors=color)
plt.title("Student data")
plt.show()