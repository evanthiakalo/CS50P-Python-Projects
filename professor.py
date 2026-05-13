import random
def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass
def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError
    if level==1:
        return random.randint(0, 9)
    elif level==2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

def main():
    level = get_level()
    score = 0


    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x+ y
        tries = 0
        while True:
            try:
                name = int(input(f"{x} + {y} = "))
            except ValueError:
                print ("EEE")
                tries +=1
                if tries ==3:
                    print(answer)
                    break
                continue
            if name== answer:
                score +=1
                break
            else:
                print("EEE")
                tries +=1
                if tries== 3:
                    print (answer)
                    break
    print(f"Score:{score}")
if __name__=="__main__":
    main()
