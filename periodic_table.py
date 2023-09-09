import periodictable as pt
atomic_no=int(input("Enter the atomic no of Element:: "))
element=pt.elements[atomic_no]
print('Atomic Number: ',element.number)
print('Symbol: ',element.symbol)
print('Name: ',element.name)
print('Atomic Mass: ',element.mass)
print('Density: ',element.density)
