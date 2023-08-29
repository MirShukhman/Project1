use master

create database BookLibraryManagment

use BookLibraryManagment

create table Books
(ID int primary key identity(1,1)
,title varchar(100)not null
,author varchar(100) not null
,pub_year int
,loan_type int not null
)

select * from Books

create table Customers
(ID int primary key identity(1,1)
,name varchar(100) not null
,city varchar(100)
,age int 
)

select * from Customers

create table Loans
(custID int foreign key references Customers(ID) 
,bookID int foreign key references Books(ID) 
,loan_Date date not null
,return_Date date
)

select * from Loans

