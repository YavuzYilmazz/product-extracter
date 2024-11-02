from config import Database

def main():
    db = Database()
    db.test_connection()

    test_record = {
        "title": "hi"
    }
    db.insert_record(test_record)

    db.close()

if __name__ == "__main__":
    main()
