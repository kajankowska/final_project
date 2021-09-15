from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register/')
def form():
    return render_template('register.html')


@app.route('/options/', methods=["POST", "GET"])
def fill():
    if request.method == "POST":
        print(dict(request.form))
    return render_template('options.html')


@app.route('/generator/', methods=["POST", "GET"])
def processing():
    print(dict(request.form))
    return render_template('plan_generator.html')


@app.route('/mealplan/')
def result():
    return render_template('meal_plan.html')


@app.route('/endofreg/')
def regend():
    return render_template('end_of_register.html')


if __name__ == '__main__':
    app.run(debug=True)
