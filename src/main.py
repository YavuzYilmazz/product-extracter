from config import Database
from classes.reader import Reader

def main():
    db = Database()
    db.test_connection()

    reader = Reader("sample.xml")
    products = reader.parse_xml()

    for product in products:
        db.insert_record(product)

    db.close()

if __name__ == "__main__":
    main()
