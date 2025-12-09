# CREATE DATABASE
CREATE DATABASE databasename;
==> SHOW DATABASES;

# DELETE DATABASE
DROP DATABASE databasename;

# The SQL BACKUP DATABASE Statement
The BACKUP DATABASE statement is used in SQL Server to create a full back up of an existing SQL database.
Syntax :
BACKUP DATABASE databasename
TO DISK = 'filepath';


Example
Get your own SQL Server
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak';

# CREATE TABLE

CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);

EXAMPLE :
 CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

The PersonID column is of type int and will hold an integer.

The LastName, FirstName, Address, and City columns are of type varchar and will hold characters, and the maximum length for these fields is 255 characters.

The empty "Persons" table will now look like this:
PersonID 	LastName 	FirstName 	Address 	City
  	  	  	 
# INSERT TABLE

Specify both the column names and the values to be inserted:

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

Example :

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

