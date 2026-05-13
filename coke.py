amount_due = 50
while amount_due >0:
    print("Amount Due:",amount_due)
    x = int(input("Insert coin: "))
    if x==10 or x==5 or x==25:
        amount_due = amount_due -x
    if amount_due<=0:
        change = -amount_due
        print ("Change Owed:", change)
