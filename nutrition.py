def main():
    fruit = input("Item: ").strip().casefold()
    nutrition = {
        "apple": 130,
        "avocado": 50,
        "pear": 100,
        "sweet cherries": 100,
        "kiwifruit": 90
    }

    if fruit in nutrition:
        print(f"Calories: {nutrition[fruit]}")

main()

