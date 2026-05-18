country_code = {'India' : '0091',
'Australia' : '0025',
'Nepal' : '00977'}

#search dictionary for country code of india
print("Country code for india-")
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of japan
print("Country code for japan-")
print(country_code.get('Japan', 'Not Found'))