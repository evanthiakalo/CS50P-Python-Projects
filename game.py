import random
while True:
    try:
        level = int(input("level: "))
        if level >0:
            break
    except ValueError:
        pass
secret = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess<=0:
            continue
    except ValueError:
        continue
    if guess < secret:
        print ("Too small!")
    elif guess> secret:
        print("Too large!")
    else:
        print("Just right!")
        break
