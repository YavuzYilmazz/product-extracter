from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

class Database:
    def __init__(self, db_name="lonca"):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db['products']

    def insert_record(self, record):
        result = self.collection.insert_one(record)
        print(f"Record inserted with ID: {result.inserted_id}")

    def test_connection(self):
        try:
            self.client.list_database_names()
            print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def close(self):
        self.client.close()
