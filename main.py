from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')
  
@app.route('/greet', methods=["POST", "GET"])
def greet():
  if request.method == "POST":
    name = request.form["name_input"]
    gpa = request.form["gpa_input"]
    college_recommendation = recommend_a_college(float(gpa))
    return render_template('results.html',name=name,gpa=gpa,college_recommendation=college_recommendation)
  else:
    return render_template('index.html')


@app.route('/subpage')
def subpage():
  return '<h3>This is a subpage!!!</h3>'

@app.route('/<string:name>')
def hello_name(name):
      return render_template('index.html',name=name)

@app.route('/<string:gpa>')
def gpa_is(gpa):
      return render_template('index.html',gpa=gpa)

def recommend_a_college(gpa):
  if gpa > 3.5:
    return 'Harvard'
  else:
    return 'BMCC'

app.run(host='0.0.0.0', port=81)