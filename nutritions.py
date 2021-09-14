import requests
import csv
import ast

meals = {}

with open("key.txt") as file:
    key = file.readlines()[0]

exc = "Drink, Mojito, Wine, Vodka, Cocktail, Rum, Whisky, Lemonade, Dip, Cake"

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
    for line in rowdata["items"]:
        meal = line["value"]
        mealplanid = line["mealPlanId"]
        slot = line["slot"]
        day = line["day"]
        ast.literal_eval
        meal_dict = ast.literal_eval(line["value"])
        meal_id = meal_dict["id"]
        meal_title = meal_dict["title"]
        dish_menu_data = [mealplanid, day, slot, meal_title]
        meals[meal_id] = dish_menu_data
