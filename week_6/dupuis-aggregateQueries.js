/*
============================================
; Title: dupuis-aggregateQueries.js
; Author: Jocelyn Dupuis
; Date: 09/11/2023
; Description: Assignment 6.2 - Aggregate Queries
============================================
*/

// Load houses.js script 
load ('houses.js')

// Query to show a list of documents in the houses collection
db.houses.find()

// Query to show a list of documents in the student's collection
db.students.find()

// Query to add a document to the student's collection
db.students.insertOne({ firstName: 'Jocelyn', lastName: 'Dupuis', studentId: 's1019', houseId: 'h1010'})

// Query tp prove the document was added to the user's collection
db.students.find({"studentId": 's1019'})

// Query to delete the above student
db.students.deleteOne({"studentId": 's1019'})

// Query to prove the document was deleted from the user's collection
db.students.find({"lastName": "Dupuis"})

// Query to show a list of students by house
db.students.aggregate( [ { $lookup: { from: "houses", localField: "houseId", foreignField: "houseId", as: "house_info" }}])  

// Query to show a list of students by house Gryffindor
db.students.aggregate( [ { $lookup: { from: "houses", localField: "houseId", foreignField: "houseId", as: "house_info" }}, { $match: { "house_info.houseId": "h1007" }}])

// Query to show a list of students for the Eagle Mascot
db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } }, 
    { $match: {"mascot": "Eagle"}} ] )