import pickle

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# ---------------------------------------------------------
# Web site
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():

    return render_template("data.html")


@app.route("/model" , methods=["POST"])
def model():

    

    creditscore = request.form["CreditScore"]
    if creditscore == "":
        creditscore = 650
    creditscore = float(creditscore)

    annualincome = request.form["AnnualIncome"]
    if annualincome == "":
        annualincome = 72000
    annualincome = float(annualincome)

    currentloanamount = request.form["CurrentLoanAmount"]
    if currentloanamount == "":
        currentloanamount = 30
    currentloanamount = float(currentloanamount)
    prediction = 0

    yearsonjob = 5.9

    X = [[currentloanamount ,creditscore, yearsonjob, annualincome, 0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0]]

    print(X)

    filename = 'model.save'
    loaded_model = pickle.load(open(filename, 'rb'))

    prediction = loaded_model.predict(X)[0]
    if prediction == 1:
        approved = "Approved"

    else:
        approved= "Not Approved"


    print(prediction)

    return render_template("index.html", prediction = approved)



if __name__ == "__main__":
    app.run()


    
