import requests
import ast


class MealPlan:
    def __init__(self):
        self.key = ""
        self.meals = {}
        self.nutritions = {}
        self.recipeid = []
        self.images = {}
        self.imageid = []
        self.userdata = {}
        self.options = {}
        self.selected = {}

    def apikey(self):
        with open("key.txt") as file:
            self.key = file.readlines()[0]

    def get_api_data(self, calories, diet_type, exclude):

        exclude = exclude.replace(" ", "").title()
        exc = "Drink,Mojito,Wine,Vodka,Cocktail,Rum,Whisky,Lemonade,Dip,Cake,Syrup," + exclude

        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

        querystring = {"timeFrame": "week", "targetCalories": calories, "diet": diet_type,
                       "exclude": exc}

        headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': self.key
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        rowdata = response.json()
        return rowdata

    def dict_save(self, rowdata):
        weekly_menu = []
        for line in rowdata["items"]:
            meal = line["value"]
            slot = line["slot"]
            day = line["day"]
            ast.literal_eval
            meal_dict = ast.literal_eval(line["value"])
            meal_id = meal_dict["id"]
            meal_title = meal_dict["title"]
            dish_menu_data = [day, slot, meal_title]
            weekly_menu.append(dish_menu_data)
            self.meals[meal_id] = dish_menu_data

    def get_nutritions(self):
        self.recipeid = list(self.meals)

        headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': self.key
        }

        for line in self.recipeid:
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/nutritionWidget.json" \
                .format(line)
            response = requests.request("GET", url, headers=headers)
            output = response.json()
            self.nutritions[line] = {"calories": output["calories"],
                                     "carbs": output["carbs"],
                                     "fat": output["fat"],
                                     "protein": output["protein"]}

    def get_images(self):
        self.imageid = list(self.meals)

        headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': self.key
        }

        for line in self.recipeid:
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{}/information".format(line)
            response = requests.request("GET", url, headers=headers)
            collection = response.json()
            self.images[line] = {"image": collection["image"]}


mp = MealPlan()
mp.apikey()
