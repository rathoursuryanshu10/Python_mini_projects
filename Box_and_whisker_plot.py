import matplotlib.pyplot as plt

data=[25,30,35,40,45,50,55,60,65,70,75]

box_color='dodgerblue'
median_color='red'
whisker_color='green'
flier_color='purple'

plt.boxplot(data,boxprops={'color':box_color},medianprops={'color':median_color},whiskerprops={'color':whisker_color},flierprops={'markerfacecolor':flier_color})
plt.xlabel('Data')
plt.ylabel('value')
plt.title('Colored Box and whisker Plot')
