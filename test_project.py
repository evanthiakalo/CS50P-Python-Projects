from project import calculate_bmi, bmi_category, view_daily_summary, meals

def test_calculate_bmi():
    result = calculate_bmi (85, 1.80)
    assert round (result, 2) == 26.23

def test_bmi_category():
    assert bmi_category(16) == "Underweight"
    assert bmi_category(23) == "Healthy weight"
    assert bmi_category(28) == "Overweight"
    assert bmi_category(34) == "Obesity"

def test_view_daily_summary():
    meals.clear()
    meals.append({
        "name": "Chicken",
        "calories": 400,
        "protein": 30,
        "carbs": 20,
        "fat": 10
    })
    view_daily_summary()
    assert meals [0] ["name"] == "Chicken"

