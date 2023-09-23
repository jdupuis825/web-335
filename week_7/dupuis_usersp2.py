#-----------------------------------------
# Title: dupuis_usersp2.py
# Author: Jocelyn Dupuis
# Date: 09/19/2023
# Description: Python with MongoDB - Part 2
#-----------------------------------------


# Imports MongoClient
from pymongo import MongoClient

# Imports datetime
from datetime import datetime

# Imports connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.t2iiezr.mongodb.net/web335DBretryWrites=true&w=majority")

# Variable declared to access web335DB
db = client["web335DB"]

# Create a new user document
new_composer = {"firstName": "Florence", "lastName": "Price", "employeeId": "1014", "email": "florenceprice@me.com", "dateCreated": datetime.now()}

# Insert the newly created document
db.users.insert_one(new_composer)

# Display the newly created document
print(db.users.find_one({"lastName": 'Price'}))

# Display an empty line 
print("")

# Update the email address of the new document
db.users.update_one({"firstName":"Florence"},{"$set":{"email":"florenceprice@me.com"}})

# Display the updated document 
print(db.users.find_one({"lastName": 'Price'}))

# Display an empty line 
print("")

# Delete the newly created document 
db.users.delete_one({'firstName':'Florence'})

# Attempt to print the newly created document to show it was deleted
print(db.users.find_one({"lastName": 'Price'}))

