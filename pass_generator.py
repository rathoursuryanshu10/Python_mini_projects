import random as rn
char=input("Enter character for your password::")
# char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvvwxyz0123456789!@#$%^&*_"
pass_len=int(input("Enter the lenght of the password:: "))
pass_count=int(input("Enter the count of passwords:: "))
for i in range(0,pass_count):
    password=""
    for j in range(0,pass_len):
        pass_char=rn.choice(char)
        password=password+pass_char 
    print("The generated password = ",password)
