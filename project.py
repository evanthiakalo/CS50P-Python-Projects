meals = []

def display_menu():
    print("\n HealthPilot Menu")
    print("1. Add Meal")
    print("2. View Daily Summary")
    print("3. Calculate BMI")
    print ("4. Exit")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round (bmi, 2)

def bmi_category (bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy weight"
    elif bmi< 30:
        return "Overweight"
    else:
        return "Obesity"

def add_meal():
    name = input("Enter meal name: ")
    calories = float(input("Enter calories: "))
    protein = float(input("Enter protein (g): "))
    carbs = float(input("Enter carbs (g): "))
    fat = float(input("Enter fat (g): "))

    meal = {
        "name": name,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    }
    meals.append(meal)
    print(f"{name} added succesfully!")



def view_daily_summary():
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for meal in meals:
        total_calories += meal.get ("calories", 0)
        total_protein += meal.get ("protein", 0)
        total_carbs += meal.get ("carbs", 0)
        total_fat += meal.get ("fat", 0)
    print("\n Nutrition Summary")
    print (f"Total Calories: {total_calories}")
    print(f"Total Protein: {total_protein}g")
    print(f"Total Carbs: {total_carbs}g")
    print(f"Total Fat: {total_fat}g")


def main():
    print("Welcome to HealthPilot!")
    while True:
        display_menu()
        choice = input("\n Choose an option: ").strip().lower()
        if choice == "1" or choice == "add meal":
            add_meal()
        elif choice == "2" or choice == "view daily summary":
            view_daily_summary()
        elif choice == "3" or choice == "calculate bmi":
            try:
                weight = float(input("Enter your weight in kg: "))
                height = float (input("Enter your height in meters: "))
                bmi = calculate_bmi (weight, height)
                category = bmi_category(bmi)
                print(f"Your BMI is {bmi}")
                print(f"Category: {category}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == "4" or choice == "exit":
            print("Thank you for using HealthPilot! See you next time!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
