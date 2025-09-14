userdata = float(input("Write the number you want to convert: "))
print(userdata)
convertedFrom = input("Converted From (eg. 'km','m', 'cm','mm',') ")
convertedTo = input("Converted To (eg. 'km','m', 'cm','mm',') ")

if convertedFrom == "km":
    if convertedTo == "km":
        print(userdata)
    elif convertedTo == "m":
        print(userdata * 1000)
    elif convertedTo == "cm":
        print(userdata * 100000)
    else:
        print(userdata * 10000000)
elif convertedFrom == "m":
    if convertedTo == "km":
        print(userdata / 1000)
    elif convertedTo == "m":
        print(userdata)
    elif convertedTo == "cm":
        print(userdata * 100)
    else:
        print(userdata * 1000)
elif convertedFrom == "cm":
    if convertedTo == "km":
        print(userdata / 100000)
    elif convertedTo == "m":
        print(userdata / 100)
    elif convertedTo == "cm":
        print(userdata)
    else:
        print(userdata * 10)
else:
    if convertedTo == "km":
        print(userdata / 10000000)
    elif convertedTo == "m":
        print(userdata / 1000)
    elif convertedTo == "cm":
        print(userdata / 10)
    else:
        print(userdata)
