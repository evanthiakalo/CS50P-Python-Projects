import inflect
p = inflect.engine()
names = []
while True:
    try:
        names.append(input(" "))
    except EOFError:
        break
result = p.join(names)
print(f"Adieu, adieu, to {result}")
