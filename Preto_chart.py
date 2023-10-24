import matplotlib.pyplot as plt
categories=['Category A', 'Category B', 'Category C','Category D', 'Category E']
values=[50,30,20,15,10]

total=sum(values)
cumulative_percentage=[100*sum(values[:i+1])/total for i in range(len(values))]

fig,ax1=plt.subplots()

ax1.bar(categories,values,color='blue')
ax1.set_xlabel('Categories')
ax1.set_ylabel('Frequency',color='blue')
ax1.tick_params(axis='y',labelcolor='blue')

ax2=ax1.twinx()
ax2.plot(categories,cumulative_percentage,color='red',marker='o')
ax2.set_ylabel('Cumulative Percentage (%)',color='red')
ax2.tick_params(axis='y',labelcolor='red')

plt.xticks(rotation=45)
plt.title('Pareto Chart')
plt.show()
