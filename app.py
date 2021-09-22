from flask import Flask, render_template, request
from meal_plan import mp


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/project/')
def project_history():
    return render_template('project_history.html')


@app.route('/register/')
def form():
    return render_template('register.html')


@app.route('/endofreg/', methods=["POST", "GET"])
def regend():
    if request.method == "POST":
        mp.userdata = dict(request.form)
    return render_template('end_of_register.html')


@app.route('/options/', methods=["POST", "GET"])
def fill():
    return render_template('options.html')


@app.route('/generator/', methods=["POST", "GET"])
def processing():
    if request.method == "POST":
        mp.options = dict(request.form)
        rowdata = mp.get_api_data(request.form["calories"], request.form["diet type"], request.form["exc"])
        mp.dict_save(rowdata)
        mp.get_nutritions()
        mp.get_images()
    return render_template('plan_generator.html')


@app.route('/mealplan/')
def result():
    print(mp.meals)
    print(mp.images)
    print(mp.nutritions)
    return render_template('meal_plan.html', mealplan=mp.meals, nutritions=mp.nutritions, images=mp.images)


@app.route('/summary/', methods=["POST", "GET"])
def theend():
    mp.selected = dict(request.form)
    print(mp.selected)
    return render_template('final.html',
                           login=mp.userdata['login'],
                           ward=mp.userdata['ward'],
                           wing=mp.userdata['wing'],
                           cutlery=mp.options['cutlery'],
                           calories=mp.options['calories'],
                           mealsnr=mp.options['meals_nr'],
                           diet=mp.options['diet type'],
                           beverage=mp.options['beverage'],
                           exc=mp.options['exc'],
                           selection=mp.selected)


if __name__ == '__main__':
    app.run(debug=True)
