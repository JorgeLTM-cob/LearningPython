import re

def getNumbers(string):
    array = re.findall(r'[0-9]+', string)
    return array

string = "1234"
array = getNumbers(string)
cadena = ''
for elem in array:
    cadena += elem
print(cadena)
