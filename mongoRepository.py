from repository import Repository
from pymongo import MongoClient

print ("hello")

class MongoRepository(Repository):

    def __init__(self):
        try:
            self.connect = MongoClient()
            self.db = self.connect.demoDB
            self.collection = self.db.demoCollection
        except:
            client = None
            pass

    def insert(self, data):
        document1 = {
            "name": "John",
            "age": 24,
            "location": "New York"
        }
        self.collection.insert_one(document1)
        cursor = self.collection.find()
        for record in cursor:
            print(record)
        pass

    def delete(self, condition):
        pass

    def update(self, data, comdition):
        pass