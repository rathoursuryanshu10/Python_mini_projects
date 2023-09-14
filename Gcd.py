a=int(input("a= "))
b=int(input("b= "))

"""if a>=b:
    if a%b==0:
        hcf=b
        #print("HCF= ",hcf)
    else:
        for i in range(1,b):
            if b%i==0 and a%i==0:
                hcf=i
    print("HCF= ",hcf)
else:
    if b%a==0:
        hcf=a
    else:
        for i in range(1,a):
            if b%i==0 and a%i==0:
                hcf=i
    print("HCF = ",hcf)
"""
"""
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print("HCF = ",a)
"""
def gcd():
    
    if(b!=0):
        return (b,a%b)
    else:
        return a
print(gcd(a))
