def power(base, exp):
    rst = 1
    for i in range(exp):
        rst = rst *base
    return rst
base = float(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
rst = power(base, exp)
print(f"{base} to the power  {exp}  =  {rst}")
