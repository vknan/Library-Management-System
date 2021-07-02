# Library-Management-System
LMS-Library Management System.
This LMS is very useful to Manage Books in Library. It can handle to 
- add books: This includes to register a new book and add it to database.
- delete books: Delete books registered and issued books.
- view book list: View complete books available in library
- issue book: Issue book to student 
- return book: Return book from student to library.

main.py - This includes a main file that calls all the functionalities available. run it!!!

#### Before Running it create a local database with the following commands and change username, mypass in the addbooks, deletebooks, viewbook, issuebook, returnbook files.
- create database db;
- create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
- create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
