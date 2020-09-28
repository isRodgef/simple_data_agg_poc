from flask import Flask, request
from mongoRepository import MongoRepository

app = Flask(__name__)

@app.route("/sendPatientData", methods = ['POST'])
def loadData():
    print (request.get_json())
    return "",404
    mongo_connector = MongoRepository()
    mongo_connector.insert({})
    return  "",200

if __name__ == '__main__':
    app.run()