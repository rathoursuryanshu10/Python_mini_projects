import matplotlib.pyplot as plt
labels=['Step 1','Step 2','Step 3','Step 4','Step 5']
values=[100,75,50,30,10]

commulative_values=[sum(values[:i+1]) for i in range(len(labels))]
colors=['blue','green','yellow','red','purple']
fig,ax=plt.subplots()
for i in range(len(labels)):
    ax.fill_betweenx([i,i+1],0,commulative_values[i],step='mid',alpha=0.7,color=colors[i])
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel('Conversion Rate')

for i,value in enumerate(commulative_values):
    ax.annotate(str(value),xy=(value,i),xytext=(5,5),textcoords='offset points')
plt.title('Funnel Chart ')
plt.show()
