# 0x00. AirBnB clone - The console.

<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220301%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220301T090116Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=725a3f3b103060f5c926540345bcde9afe5a24325b8426b620e0005802c7e7fa">

## The project is to create a clone of AirBNB website.

### First step: Write a command interpreter to manage our AirBnB objects.

This is the first step towards building our first full web application: the AirBnB clone.

## What’s a command interpreter?
Do you kown Shell? It’s exactly the same but limited to a specific use-case.

## After 4 months, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
* A website (the front-end) that shows the final product to everybody: static and dynamic.
* A database or files that store data (data = objects).
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).


# The command interpretor.

## Execution.

the command interpreter can be run:

* in interactive mode: `$ ./console.py`.
*  in non-interactive mode: (like the Shell project in C) `$ echo "help" | ./console.py`.

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`.

## Commands.

* `create`: Creates a new instance of BaseModel, saves it and prints the id.
* `show`: Prints the string representation of an instance based on the class name and id.
* `destroy`: Deletes an instance based on the class name and id.
* `all`: Prints all string representation of all instances based or not on the class name.
* `update`: Updates an instance based on the class name and id by adding or updating attribute.
* `quit`: exit thr program

## Exemples.

* `$ create BaseModel`.
* `$ show BaseModel 1234-1234-1234`.
* `$ destroy BaseModel 1234-1234-1234`.
* `$ all BaseModel`.
* `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.