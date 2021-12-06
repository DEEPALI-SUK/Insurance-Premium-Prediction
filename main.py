from flask import Flask, request, render_template
import util

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', expense="")

@app.route('/predict_expense', methods=['POST'])
def predict_expense():
  if request.method == 'POST':
    age= request.form['age']
    bmi= float(request.form['bmi'])
    children= request.form['children']
    gender= request.form.get('gender')
    smoke= request.form.get('smoke')
    print(smoke)
    print(gender)

    location= request.form.get('location')
    print(location)
    expense= util.get_expense(age,bmi,children,gender,smoke,location)
    print(expense)
    return render_template('index.html', expense=expense)
  else:
    return render_template('index.html', expense="")


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)