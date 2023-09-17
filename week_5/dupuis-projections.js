/*
============================================
; Title: dupuis-projections.js
; Author: Jocelyn Dupuis
; Date: 09/07/2023
; Description: Routing for composers API assignment
============================================
*/

// Query to add new user to user's collection
db.users.insertOne({ "firstName": "Pyotr", "lastName": "Tchaikovsky", "employeeId": "1013", "email": "ptchaikovsky@me.com", "dateCreated": new Date()})

// Query to update Mozart's email address
db.users.updateOne({"lastName": "Mozart"}, {$set: {"email": "mozart@me.com"}})

// query to find/prove that Mozart's email address was updated
db.users.find({"email": "mozart@me.com"})

// Query to list all documents in the user's collection only displaying fistName, lastName, and email address
db.users.aggregate( [ { $project : { "_id": 0, "firstName": 1, "lastName": 1, "email": 1 }}])


