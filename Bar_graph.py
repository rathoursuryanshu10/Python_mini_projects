from bokeh.plotting import figure,show
from bokeh.io import output_notebook

categories=['Categories 1', 'Categories 2', 'Categories 3', 'Categories 4','Categories 5']
values=[10,25,15,40,5]

p=figure(x_range=categories,title="Bar Graph Example",x_axis_label='Categories',y_axis_label='Values')
p.vbar(x=categories,top=values,width=0.5)

output_notebook()
show(p)
