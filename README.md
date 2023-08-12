# AirBnB_clone

## Description:

The AirBnB_clone is a web application project which its goal is to deploy on your server a simple copy of the AirBnB website.

This web application is composed by:
  -  A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
  -  A website (the front-end) that shows the final product to everybody: static and dynamic
  -  A database or files that store data (data = objects).
  -  An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).
 
> In this repository, we will focus only on **the command interpreter** and **file storage**.

## The command interpreter (The console)

*Do you know the Shell?* Well it’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
  1.  Create a new object (ex: a new User or a new Place)
  2.  Retrieve an object from a file, a database etc…
  3.  Do operations on objects (count, compute stats, etc…)
  4.  Update attributes of an object
  5.  Destroy an object

## Getting started

You can interact with the program if you follow these steps:

> **Phase 1**: Clone the repo using the following command

```` 
git clone https://github.com/bouhvli/AirBnB_clone.git
````

> **Phase 2**: Change your current directory to AirBnB_clone

```` 
cd ./AiBnB_clone
````

> **Phase 3**: Execute the console file

```` 
./console.py
````

> **Phase 4**: Enter command you want use **help** command to the availabe commands after you see "(hbnb) " 

```` 
(hbnb) help
````

## Example

````
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all

        Prints all string representation of
        all instances based or not on the class name.

(hbnb) all
["[BaseModel] (0891a4c5-e7fc-4b11-a1d0-d98016c298a9) {'id': '0891a4c5-e7fc-4b11-a1d0-d98016c298a9', 'created_at': datetime.datetime(2023, 8, 12, 5, 33, 15, 183936), 'updated_at': datetime.datetime(2023, 8, 12, 5, 33, 15, 183978)}","[BaseModel] (23a6acf3-ed61-4f2b-8bbc-0c347c2ece57) {'id': '23a6acf3-ed61-4f2b-8bbc-0c347c2ece57', 'created_at': datetime.datetime(2023, 8, 12, 5, 10, 25, 884661), 'updated_at': datetime.datetime(2023, 8, 12, 5, 10, 25, 884691)}", "[Place] (7f5ad8bd-cb46-413c-9a52-a0972adee4a7) {'id': '7f5ad8bd-cb46-413c-9a52-a0972adee4a7', 'created_at': datetime.datetime(2023, 8, 12, 5, 10, 35, 357701), 'updated_at': datetime.datetime(2023, 8, 12, 5, 10, 35, 357722)}", "[User] (aee51514-e444-4d68-b63f-c169b75cec00) {'id': 'aee51514-e444-4d68-b63f-c169b75cec00', 'created_at': datetime.datetime(2023, 8, 12, 5, 10, 30, 752718), 'updated_at': datetime.datetime(2023, 8, 12, 6, 19, 9, 978598), 'FirstName': 'Youssef'}"]

(hbnb) all Place
["[Place] (7f5ad8bd-cb46-413c-9a52-a0972adee4a7) {'id': '7f5ad8bd-cb46-413c-9a52-a0972adee4a7', 'created_at': datetime.datetime(2023, 8, 12, 5, 10, 35, 357701), 'updated_at': datetime.datetime(2023, 8, 12, 5, 10, 35, 357722)}"]

(hbnb) all DS
** class doesn't exist **

(hbnb) all BaseModel
["[BaseModel] (0891a4c5-e7fc-4b11-a1d0-d98016c298a9) {'id': '0891a4c5-e7fc-4b11-a1d0-d98016c298a9', 'created_at': datetime.datetime(2023, 8, 12, 5, 33, 15, 183936), 'updated_at': datetime.datetime(2023, 8, 12, 5, 33, 15, 183978)}", "[BaseModel] (23a6acf3-ed61-4f2b-8bbc-0c347c2ece57) {'id': '23a6acf3-ed61-4f2b-8bbc-0c347c2ece57', 'created_at': datetime.datetime(2023, 8, 12, 5, 10, 25, 884661), 'updated_at': datetime.datetime(2023, 8, 12, 5, 10, 25, 884691)}"]

(hbnb) create BaseModel
ecc717d4-54cf-4c87-9fba-c804272329b2

(hbnb) create
** class name missing **

(hbnb) show ecc717d4-54cf-4c87-9fba-c804272329b2
** class doesn't exist **

(hbnb) show BaseModel ecc717d4-54cf-4c87-9fba-c804272329b2
[BaseModel] (ecc717d4-54cf-4c87-9fba-c804272329b2) {'id': 'ecc717d4-54cf-4c87-9fba-c804272329b2', 'created_at': datetime.datetime(2023, 8, 12, 6, 29, 39, 595541), 'updated_at': datetime.datetime(2023, 8, 12, 6, 29, 39, 595575)}

(hbnb) update BaseModel ecc717d4-54cf-4c87-9fba-c804272329b2 Name Josh

(hbnb) destroy BaseModel 0891a4c5-e7fc-4b11-a1d0-d98016c298a9

(hbnb) quit
````
