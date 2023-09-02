from forex_python.converter import CurrencyRates
c=CurrencyRates()
from_currency=input("From_currency:: ").upper()
amount=int(input("Enter the amount:: "))
to_currency=input("To_currency:: ").upper()
print(from_currency,"to" , to_currency," ",amount)
result=c.convert(from_currency,to_currency,amount)
print(result)

