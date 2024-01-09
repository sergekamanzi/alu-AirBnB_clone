AirBnB clone The console


The project's objective is to install a basic replica of the AirBnB website on a server. Only a portion of the features will be implemented in order to cover all of the essential ideas of the higher level programming course.

First action: To control your AirBnB objects, write a command interpreter. Because it will apply the skills you develop in this project for all subsequent projects, this first step is crucial: Front-end, database storage, API, and HTML/CSS templating in


What is an interpreter for commands? Remember the Shell? It is same but restricted to a certain use-case. In this instance, our goal is to be able to oversee the project's


Make a new object (for example, a new Place or User). Get an item out of a database, file, etc. Apply operations (such as count and compute stats) to objects. Modify an object's properties Eliminate an Execution You could operate in interactive mode as follows:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
Commands:
create - create an object
show - show an object (based on id)
destroy - destroy an object
all - show all objects, of one type or all types
update - Updates an instance based on the class name and id
quit/EOF - quit the console
help - see descriptions of commands
To start console type in shell

AirBnB_clone$ ./console.py
(hbnb)
Create
To create an object use format "create " ex:

(hbnb) create BaseModel
Show
To show an instance based on the class name and id. Ex:

(hbnb) show BaseModel 1234-1234-1234.
Destroy
To Delete an instance of an object use "destroy id". Ex:

(hbnb) destroy BaseModel 1234-1234-1234.
All
all or all Ex:

(hbnb) all or all State
Update
Updates an instance based on the class name and id:

(hbnb) update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
Quit
quit or EOF

Help
help or help Ex:

(hbnb) help or help quit
 Defines quit option
 (hbnb)
 Supported classes:
 BaseModel
 User
 State
 City
 Amenity
 Place
 Review
 Authors
 Mary Doh
