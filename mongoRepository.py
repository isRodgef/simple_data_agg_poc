from repository import Repository
from pymongo import MongoClient

print ("hello")

class MongoRepository(Repository):
    cleint = MongoClient("127.0.0.1")
    def insert(self, data):
        pass

    def delete(self, condition):
        pass

    def update(self, data, comdition):
        pass