import requests
import csv
import ast

meals = {}

with open("key.txt") as file:
    key = file.readlines()[0]

exc = "Drink, Mojito, Wine, Vodka, Cocktail, Rum, Whisky, Lemonade, Dip, Cake"

with open("meals.json", "w") as file:
    file.write("")

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

    querystring = {"timeFrame": "week", "targetCalories": "2400", "diet": "vegetarian",
                   "exclude": exc}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rowdata = response.json()

with open("dane.csv", "w", newline="") as file:
    writer = csv.writer(file)
    weekly_menu_data = []
    for line in rowdata["items"]:
        meal = line["value"]
        mealplanID = line["mealPlanId"]
        slot = line["slot"]
        day = line["day"]
        ast.literal_eval
        meal_dict = ast.literal_eval(line["value"])
        meal_id = meal_dict["id"]
        meal_title = meal_dict["title"]
        dish_menu_data = [mealplanID, day, slot, meal_title]
        meals[meal_id] = dish_menu_data
        weekly_menu_data.append(dish_menu_data)
    writer.writerows(weekly_menu_data)
