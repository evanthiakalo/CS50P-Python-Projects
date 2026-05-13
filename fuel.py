while True:
    try:
        n = input("Fraction:" )
        X , Y = n.split ("/")
        X = int(X)
        Y = int (Y)
        if X<0 or Y<=0 or X>Y:
            continue
        percent = round ((X/Y) *100)
        if percent <=1:
            print("E")
        elif percent>=99:
            print("F")
        else:
            print(f"{percent}%")
        break
    except(ValueError, ZeroDivisionError):
        continue
