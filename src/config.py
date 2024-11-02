from pymongo import MongoClient
from dotenv import load_dotenv
from classes.product import Product
from datetime import datetime
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

        # Use stock_code to check if the product already exists
        existing_product = self.collection.find_one({"stock_code": record["stock_code"]})

        if existing_product:
            # Update the existing product but only change updatedAt and other specified fields
            record["updatedAt"] = datetime.now()  # Set updatedAt to the current time
            self.collection.update_one(
                {"stock_code": record["stock_code"]},
                {"$set": record}  # Update all fields, including updatedAt
            )
            print(f"Updated product with stock_code: {record['stock_code']}, updatedAt set to current time.")
        else:
            # Insert a new record
            record["createdAt"] = datetime.now()  # Set createdAt for new records
            self.collection.insert_one(record)
            print(f"Inserted new product with stock_code: {record['stock_code']}")


    def test_connection(self):
        try:
            self.client.list_database_names()
            print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def close(self):
        self.client.close()
