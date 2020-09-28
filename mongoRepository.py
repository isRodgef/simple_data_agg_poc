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
            self.connect = None
            pass

    def insert(self, data):
        if self.connect != None:
            self.collection.insert_one(data)
            #return True
        #return False
        cursor = self.collection.find()
        for record in cursor:
            print(record)

    def delete(self, condition):
        pass

    def update(self, data, comdition):
        pass