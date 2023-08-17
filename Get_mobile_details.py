#Mobile No Details: 
import phonenumbers as pn
from phonenumbers import timezone,geocoder,carrier

def code_validation():
    j=0
    ccode=input("Enter the country code with +__ :: ")
    if (ccode[0]=="+" and (len(ccode)==3 or len(ccode)==4)):
        for i in range(1,len(ccode)):
            if(ccode[i].isdigit()):
                #print(ccode[i])
                continue
            else:
                j=1 
        if j==1 :
            print("Enter the country code + with digits only..")
        else:
            country_code=ccode
            return country_code
    else:
        print("Enter the country code with + and of 2 or 3 letters ") 

def number_validation():
    k=0
    num=str(input("Enter your phone number :: "))
    if len(num)==10 or len(num)==11:
        for i in num:
            if i.isdigit():
                continue
            else:
                k=1
        if k==1:
            print("Please enter all digits in your phone number. ")
        else:
            number=num
            return number                
    else:
        print("Please enter the phone number of 10 or 11 characters.. ")

def get_no_dedails():
    country_code=code_validation()
    #print(country_code)
    while country_code==None:
        country_code=code_validation()
    number=number_validation()
    #print(number)
    while number==None:
        number=number_validation()
    pno=country_code+number
    phoneNumber=pn.parse(pno)
    time=timezone.time_zones_for_number(phoneNumber)
    car=carrier.name_for_number(phoneNumber,"en")
    registration=geocoder.description_for_number(phoneNumber,"en")
    print("Phone Number:: ",phoneNumber)
    print("Time Zone:: ",time)
    print("Service Provider:: "+car)
    print("Location:: "+registration)

get_no_dedails()
