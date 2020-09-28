from flask import   Flask

app = Flask(__name__)

@app.route("/getPatientData", methods = ['POST'])
def loadData():
    return 200, ""

if __name__ == '__main__':
    app.run()