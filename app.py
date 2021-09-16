from flask import Flask, render_template, request
from meal_plan import mp, nut, im


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register/')
def form():
    return render_template('register.html')


@app.route('/endofreg/', methods=["POST", "GET"])
def regend():
    if request.method == "POST":
        personal = dict(request.form)
        userlogin = request.form['login']
        userward = request.form['ward']
        userwing = request.form['wing']
    return render_template('end_of_register.html')


@app.route('/options/', methods=["POST", "GET"])
def fill():
    return render_template('options.html')


@app.route('/generator/', methods=["POST", "GET"])
def processing():
    if request.method == "POST":
        print(dict(request.form))
        rowdata = mp.get_api_data(request.form["calories"], request.form["diet type"], request.form["exc"])
        mp.dict_save(rowdata)
        # output = nut.get_nutritions()
        # nut.nutritions_save(output)
    return render_template('plan_generator.html')


@app.route('/mealplan/')
def result():
    return render_template('meal_plan.html', mealplan=mp.meals)


@app.route('/summary/', methods=["POST", "GET"])
def theend():
    return render_template('final.html', )


if __name__ == '__main__':
    app.run(debug=True)
