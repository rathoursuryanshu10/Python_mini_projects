import matplotlib.pyplot as pyplot
labels=('Python','JavaScript','Java','C#')
sizes=(45,30,15,10)
explode=(0.1,0,0,0)
pyplot.pie(sizes,explode=explode,labels=labels,autopct='%1.f%%',shadow=True,counterclock=False,startangle=45)
pyplot.show()
