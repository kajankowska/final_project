import requests
import csv
from meal_plan import meals

nutritions = {}

with open("key.txt") as file:
    key = file.readlines()[0]

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': key
    }

recipeid = meals.keys()
for line in recipeid:
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/nutritionWidget.json".format(line)
    response = requests.request("GET", url, headers=headers)
    output = response.json()
    nutritions[line] = output


with open("wartosciodzywcze.csv", "a", newline="") as file:
    writer = csv.writer(file)
    for line in nutritions:
        cal = nutritions[line]["calories"]
        carb = nutritions[line]["carbs"]
        fat = nutritions[line]["fat"]
        protein = nutritions[line]["protein"]
        nutri_list = [line, cal, carb, fat, protein]
        writer.writerow(nutri_list)

print(output)
