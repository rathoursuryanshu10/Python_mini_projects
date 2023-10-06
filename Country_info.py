from countryinfo import CountryInfo
count=input("Enter the country name:: ")
country=CountryInfo(count)
print('The Name of the Country:',count.upper())
print('Capital is: ',country.capital())
print('Currencies are: ',country.currencies())
print('Languages are: ',country.languages())
print('Borders are: ',country.borders())
print('other Names::  ',country.alt_spellings())
