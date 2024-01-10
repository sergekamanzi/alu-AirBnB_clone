Project Description

This project is the initial step in constructing an AirBnB clone, serving as the foundation for subsequent tasks such as HTML/CSS templating,database storage, API development, and front-end integration. The primary goal is to establish a parent class, BaseModel, responsible for the initialization, serialization, and deserialization of future instances. The project also involves implementing a basic flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file. Additionally, various classes (User, State, City, Place, etc.) are created, all inheriting from the BaseModel. The first abstracted storage engine for the project, File storage, is introduced along with comprehensive unittests to validate classes and the storage engine

Command Interpreter
The command interpreter is akin to the Shell but tailored for the specific needs of our project. It enables the management of objects within the AirBnB project, allowing users to:

1.Create a new object: Generate a new User, Place, or other relevant objects.

2.Retrieve an object: Fetch an object from a file, database, or other storage mediums.

3.Perform operations on objects: Conduct operations such as counting, computing stats, and more.

4.Update attributes: Modify attributes of an existing object.

5.Destroy an object: Remove an object from the system.

How to Start

1.git clone https://github.com/your-username/AirBnB-Clone.git
2.cd AirBnB-Clone
3./console.py

How to Use

1.create: Create a new object. Example: create User

2.show: Display details of a specific object. Example: show User 1234-1234-1234

3.destroy: Remove an object. Example: destroy Place 5678-5678-5678

4.update: Modify attributes of an object. Example: update State 9876-9876-9876 name "California"

5.all: Display all objects or all objects of a specific class. Example: all or all City

6.quit: Exit the command interpreter. Example: quit


This project serves as a crucial step towards constructing a full-fledged web application, emphasizing good software design practices, maintainability, and extensibility. As development progresses, this foundation will prove instrumental in implementing more advanced features and functionalities for the AirBnB clone.

thanks to serge kamanzi and Excel Asaph
