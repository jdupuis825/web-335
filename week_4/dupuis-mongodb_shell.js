/*
============================================
; Title: dupuis-mongodb_shell.js
; Author: Jocelyn Dupuis
; Date: 09/01/2023
; Description: List of queries
============================================
*/


// Loads users from file
load ('users.js')

// Displays all documents in the user's collection
db.users.find()

// Query to find user with email address
db.users.find({ "email": "jbach@me.com" })

// Query to find user by last name
db.users.find({ "lastName": "Mozart" })

// Query to find user by first name
db.users.find({ "firstName": "Richard" })

// Query to find user by employeeId
db.users.find({ "employeeId": "1010" })