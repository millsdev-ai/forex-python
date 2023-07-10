from forex_python.converter import CurrencyRates

#Create an object of CurrencyRates class
c = CurrencyRates()

#Get the amount and currency
amount = int(input("Enter amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()

#Prints the currency conversion
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount) 

print(result)

#millsdev-ai

#rename forex_python.py to forex_python_converter.py