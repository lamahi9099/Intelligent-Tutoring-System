from flask import Flask, render_template, request, redirect, url_for, session
from owlready2 import *

# Load your ontology
onto = get_ontology("shape.owl").load()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['first_name']
        lastName = request.form['last_name']
        email = request.form['email']
        
        print(f"name: {firstName} {lastName} {email}")
        
        klass1 = onto.Student(firstName)
        klass1.email.append(email)
        klass1.firstName.append(firstName)
        klass1.lastName.append(lastName)
        
        onto.save("shape.owl")
        
        return redirect(url_for('area_of_shape'))
    return render_template('register.html')

@app.route('/area', methods=['GET', 'POST'])
def area_of_shape():
    return render_template('calculate.html')

@app.route('/calculate', methods=['POST'])
def calculateForm():
    if request.method == 'POST':
        base1 = int(request.form['base1'])
        base2 = int(request.form['base2'])
        height = int(request.form['height'])
        
        area_trapezoid = (base1 + base2) * height / 2
        
        baseOne = onto.Trapezoid('Trapezoid1')
        baseOne.base1.append(base1)
        baseOne.base2.append(base2)
        baseOne.height.append(height)
        baseOne.area.append(area_trapezoid)
        
        onto.save("shape.owl")
        
        return redirect(url_for('result', area=area_trapezoid))
    return render_template('calculate.html')

@app.route('/result')
def result():
    area = request.args.get('area')
    return render_template('result.html', area=area)

if __name__ == '__main__':
    app.run(debug=True)