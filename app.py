from flask import Flask, request
from mongoRepository import MongoRepository
from mongosanitizer.sanitizer import sanitize


app = Flask(__name__)

@app.route("/sendPatientData", methods = ['POST'])
def loadData():
    incomingData = request.get_json()
    sanitize(incomingData)

    mongo_connector = MongoRepository()
    mongo_connector.insert(incomingData)
    return  "",200

if __name__ == '__main__':
    app.run()