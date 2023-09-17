#-----------------------------------------
# Title: dupuis_usersp1.py
# Author: Jocelyn Dupuis
# Date: 09/12/2023
# Description: Python with MongoDB - Part 1
#-----------------------------------------

# Import MongoClient
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.t2iiezr.mongodb.net/web335DBretryWrites=true&w=majority")

# Connects to my web335DB
db = client['web335DB']

# Stores list of users
users = (db.users.find({}))

# Displays all documents in the user's collection
for user in db.users.find({}):
    print(user)
    breakLine()

# Displays a documents where specific employeeId is 1011
print(db.users.find_one({'employeeId': '1011'}))
breakLine()

# Displays a document where lastName is Mozart
print(db.users.find_one({'lastName': 'Mozart'}))
breakLine()