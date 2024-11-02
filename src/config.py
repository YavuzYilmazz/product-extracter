from pymongo import MongoClient
from dotenv import load_dotenv
from classes.product import Product
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

class Database:
    def __init__(self, db_name=DATABASE_NAME):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[db_name]
        self.collection = self.db[COLLECTION_NAME]

    def insert_record(self, record):
        if isinstance(record, Product):
            record = record.to_dict()
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
