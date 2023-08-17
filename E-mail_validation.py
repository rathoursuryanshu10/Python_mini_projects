email=input("Enter your email address:: ")
j=0
k=0
d=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3] =="."):
                for i in email:
                    if i.isspace():
                        k=1
                        #print(k)
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                            #print("upper")
                    elif i.isdigit():
                        continue
                    elif i== "_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                        
                if ((k==1) or (j==1) or (d==1)) :
                    print("Wrong email,Email should not use these special characters. ")
                else:
                    print("Right email..")
            else:
                print("Wrong your,Email should be placed the . symbol at right place.  ")
        else:
            print("Wrong email,There should be only one @ symbol. ")
    else:
        print("Wrong email, First letter should be Character. ")
else:
    print("Wrong email, Email should be minimum of 6 characters. ")
