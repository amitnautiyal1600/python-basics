# store data in kew pair

monthFullName = {
    "jan" : "January",
    "feb" : "Feburary",
    "mar" : "March",
    "apr" : "April",
    "may" : "May",
    "june" : "June",
    "july" : "July",
    "aug" : "August",
    "sep" : "September",
    "oct" : "October",
    "nov" : "Novemeber",
    "dec" : "December",
}

print(monthFullName["nov"])

## use pre built function

print(monthFullName.get('nov'))

## it is usefull to handle if key not exist
print(monthFullName.get('test'))
print(monthFullName.get('test', 'Note a Valid key'))

