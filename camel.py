x = input("camelCase: ")
result = ""
for letter in x:
    if letter.isupper():
        result = result + "_" + letter.lower()
    else:
        result = result + letter
print (result)
