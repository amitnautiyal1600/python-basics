# store data in key pair

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
print(monthFullName["nov"])

# use pre built function


# it is useful to handle if key not exist
print(monthFullName.get('nov'))
print(monthFullName.get('test'))
print(monthFullName.get('test', 'Note a Valid key'))

