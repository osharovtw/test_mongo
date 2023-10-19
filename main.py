import sys
from pymongo import MongoClient

if __name__ == "__main__":
    print("main.py mongo_url dbname collection")
    mongo_url = sys.argv[1]
    db_name = sys.argv[2]
    collection = sys.argv[3]
    print(f"Creating client with {mongo_url}")
    client = MongoClient(mongo_url)
    print(f"Created")
    print("executing client[db_name][collection].find()...")
    result = client[db_name][collection].find({})
    for r in result:
        print(r["_id"])
