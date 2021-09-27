#importing the libraries
import pickle
import numpy
from flask import Flask, request, render_template

#Global Variables
app = Flask(__name__)
loadedModel= pickle.load(open('diabetes.pkl','rb'))

#user defined functions
@app.route("/",methods=['Get'])
def Home():
    return render_template('index.html')

#user input commands
@app.route('/prediction',methods=['POST'])
def predict():
    name=request.form['name']
    bmi=int(request.form['bmi'])
    age=int(request.form['age'])
    glucose=int(request.form['glucose'])

    prediction=loadedModel.predict([[glucose,bmi,age]])

    if prediction ==[0]:
        prediction = 'Not Diabetic'

    else:
        prediction = 'Diabetic'

    return render_template('index.html',diagnosis_output = prediction)

#main function
if __name__=="__main__":
     app.run(debug=True)
