import seaborn as sn
import matplotlib.pyplot as plt

labels=['Category A','Category B','Category C','Category D']
sizes=[15,30,45,10]

plt.figure(figsize=(6, 6))
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=140)
plt.title("Data repesented as Pie Chart")
plt.show()
