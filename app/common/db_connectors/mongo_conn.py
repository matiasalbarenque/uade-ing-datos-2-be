from pymongo import MongoClient, errors
from decouple import config

MONGODB_SERVICE = config("MONGODB_SERVICE")
MONGODB_URI = config("MONGODB_URI")
MONGODB_DBNAME = config("MONGODB_DBNAME")
MONGODB_USERNAME = config("MONGODB_USERNAME")
MONGODB_PASSWORD = config("MONGODB_PASSWORD")
MONGODB_COLLECTION = config("MONGODB_COLLECTION")

class MongoConnector:
    def __init__(self, database_name=MONGODB_DBNAME, collection_name=MONGODB_COLLECTION):
        self.client = MongoClient(f"{MONGODB_SERVICE}{MONGODB_USERNAME}:{MONGODB_PASSWORD}{MONGODB_URI}")
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
    def check_connection(self):
        try:
            # The ping command is used to check the connection
            self.client.admin.command('ping')
            return True
        except errors.ConnectionError as e:
            print(f"Connection error: {e}")
            return False
        
    def insert_document(self, document):
        insert_result = self.collection.insert_one(document)
        return insert_result.inserted_id

    def find_document(self, query):
        return self.collection.find_one(query)

    def update_document(self, query, new_values):
        update_result = self.collection.update_one(query, new_values)
        return update_result.matched_count, update_result.modified_count

    def delete_document(self, query):
        delete_result = self.collection.delete_one(query)
        return delete_result.deleted_count

    def add_like(self, query, user_id):
        update_result = self.collection.update_one(query, {"$addToSet": {"likes": user_id}})
        return update_result.matched_count, update_result.modified_count

    def close_connection(self):
        self.client.close()
