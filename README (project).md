# HealthPilot

#### Video Demo: https://youtu.be/i_1aKKJRFGI

## Description
HealthPilot is a Python program that helps users track their daily meals and calculate their Body Mass Index (BMI). The goal of this project is to provide a simple nutrition assistant that allows users to monitor their food intake and understand their health status. The program runs in a loop with a simple menu system that allows users to choose between different options such as adding meals, viewing a summary, or calculating BMI. This makes the application interactive and easy to use.

### 1. Add Meal
Users can enter a meal with its calories, protein, carbohydrates and fat. Each meal is stored as a dictionary with keys for name, calories, protein, carbohydrates and fat. All meals are then stored inside a list which allows multiple entries during a session.

### 2. View Daily Summary
The program calculates the total calories and macronutrients (protein, carbs, fat) from all meals entered during the session.

### 3. BMI Calculator
Users can input their weight and height to calculate their BMI. The program also categorizes the result into:
- Underweight
- Healthy weight
- Overweight
- Obesity

## Design
I used functions to organize the code into separate parts, making the code more readable and easier to maintain. Each function handles a specific task such as adding meals or calculating BMI. Meals are stored in a list of dictionaries for flexible data storage. Input validation is used in some parts of the program to prevent crashes from invalid input.

## Testing
The project includes pytest tests for key functions. This ensures the program produces accurate results.

