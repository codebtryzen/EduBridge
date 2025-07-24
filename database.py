import pymongo
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read MONGO_URI
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI not found in .env file")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)

# Use the edubridge database
db = client["edubridge"]

# Example collection
scores_collection = db["scores"]

def save_user_score(username, score):
    scores_collection.insert_one({"username": username, "score": score})
    print(f"Saved score {score} for user {username}")

def get_user_scores(username):
    results = list(scores_collection.find({"username": username}, {"_id": 0}))
    return results

if __name__ == "__main__":
    save_user_score("alice", 85)
    print(get_user_scores("alice"))
