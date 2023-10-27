import itertools
print("The truth table for XNOR gate is: ")
print("A\tB\tResult")
input_comb=list(itertools.product([True,False],repeat=2))

for combination in input_comb:
    A, B=combination
    result=not (A ^ B) 
    print(f"{int(A)}\t{int(B)}\t{int(result)}")
