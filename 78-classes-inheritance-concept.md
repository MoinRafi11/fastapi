
# 78 - Classes and Inheritance Concept in Python

## 1. Introduction

Classes and inheritance are fundamental concepts in Object-Oriented Programming (OOP).

Python supports OOP, allowing developers to organize code into reusable structures, represent real-world entities, and reduce code duplication.

In this guide, we will learn about:

- Classes and objects
- Constructors
- Attributes and methods
- Inheritance
- Types of inheritance
- Method overriding
- The `super()` function
- Practical examples

## 2. What Is a Class?

A class is a blueprint for creating objects. It defines the attributes and methods that objects created from it can have.

For example, a `Car` class can define properties such as brand and color, along with actions such as starting and stopping.

### Example

```python
class Car:
    def start(self):
        print("The car has started")


car1 = Car()

car1.start()
```

**Output:**

```text
The car has started
```

### Explanation

- `class Car:` defines a class named `Car`.
- `def start(self):` defines a method.
- `car1 = Car()` creates an object of the class.
- `car1.start()` calls the method using that object.

## 3. What Is an Object?

An object is an instance of a class.

A single class can be used to create multiple objects, each with its own instance attributes.

### Example

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")


car1 = Car("Toyota", "White")
car2 = Car("BMW", "Black")

car1.display()
car2.display()
```

**Output:**

```text
Brand: Toyota
Color: White
Brand: BMW
Color: Black
```

Here, `car1` and `car2` are separate objects created from the same class.

## 4. Understanding the Constructor (`__init__`)

The `__init__()` method initializes an object's attributes when an instance is created.

It is commonly called the constructor in everyday Python discussions, although technically object creation is handled by `__new__()`, and `__init__()` initializes the created object.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Moin", 22)

print(student1.name)
print(student1.age)
```

**Output:**

```text
Moin
22
```

### Explanation

- `__init__()` runs automatically during normal instance creation.
- `self` refers to the current instance.
- `self.name` stores the name on that instance.
- `self.age` stores the age on that instance.

## 5. What Is `self` in Python?

`self` refers to the current instance of a class. It allows instance methods to access that object's attributes and other methods.

It is a naming convention rather than a reserved Python keyword, but using `self` is standard practice.

### Example

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")


employee = Employee("Moin")
employee.introduce()
```

**Output:**

```text
My name is Moin
```

When you call `employee.introduce()`, Python passes the instance to the method automatically.

## 6. What Is Inheritance?

Inheritance is an OOP feature that allows one class to inherit attributes and methods from another class.

It helps developers reuse existing code and create relationships between related classes.

The class being inherited from is called the **parent class**, **base class**, or **superclass**.

The class that inherits from it is called the **child class**, **derived class**, or **subclass**.

### Basic Syntax

```python
class Parent:
    pass


class Child(Parent):
    pass
```

Here, `Child` inherits from `Parent`.

## 7. Simple Inheritance Example

```python
class Animal:
    def eat(self):
        print("This animal eats food")


class Dog(Animal):
    def bark(self):
        print("The dog barks")


dog = Dog()

dog.eat()
dog.bark()
```

**Output:**

```text
This animal eats food
The dog barks
```

### Explanation

- `Animal` is the parent class.
- `Dog` is the child class.
- `Dog` inherits the `eat()` method from `Animal`.
- `Dog` also defines its own `bark()` method.

The `Dog` object can use both methods without duplicating the `eat()` implementation.

## 8. Types of Inheritance in Python

Python supports several inheritance patterns.

### 8.1 Single Inheritance

A child class inherits from one parent class.

```python
class Parent:
    def show(self):
        print("Parent class")


class Child(Parent):
    pass


obj = Child()
obj.show()
```

**Output:**

```text
Parent class
```

Structure:

```text
Parent
   |
   v
Child
```

### 8.2 Multiple Inheritance

A child class inherits from more than one parent class.

```python
class Father:
    def skills(self):
        print("Gardening")


class Mother:
    def talent(self):
        print("Painting")


class Child(Father, Mother):
    pass


obj = Child()

obj.skills()
obj.talent()
```

**Output:**

```text
Gardening
Painting
```

The `Child` class inherits methods from both `Father` and `Mother`.

When multiple parent classes define the same method, Python follows its Method Resolution Order (MRO) to determine which implementation is used.

### 8.3 Multilevel Inheritance

A class inherits from a child class, forming a chain of inheritance.

```python
class Grandparent:
    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):
    def car(self):
        print("Parent's car")


class Child(Parent):
    def bike(self):
        print("Child's bike")


obj = Child()

obj.house()
obj.car()
obj.bike()
```

**Output:**

```text
Grandparent's house
Parent's car
Child's bike
```

Structure:

```text
Grandparent
     |
     v
   Parent
     |
     v
   Child
```

The child can access inherited methods along the inheritance chain.

### 8.4 Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

```python
class Animal:
    def eat(self):
        print("Eating food")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
```

**Output:**

```text
Eating food
Barking
Eating food
Meowing
```

Both `Dog` and `Cat` inherit the `eat()` method from `Animal`.

### 8.5 Hybrid Inheritance

Hybrid inheritance combines two or more inheritance patterns.

```python
class A:
    def show(self):
        print("Class A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


obj = D()
obj.show()
```

**Output:**

```text
Class A
```

This example combines hierarchical and multiple inheritance.

Python's MRO ensures that the shared ancestor is handled according to its method resolution rules.

## 9. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method inherited from its parent class.

It allows a child class to customize inherited behavior.

### Example

```python
class Animal:
    def sound(self):
        print("Animals make sounds")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()
```

**Output:**

```text
Animals make sounds
Dog barks
```

The `Dog` class overrides the inherited `sound()` method.

When `dog.sound()` is called, Python uses the implementation defined in `Dog`.

## 10. Using `super()`

The `super()` function provides access to methods from a parent class according to Python's Method Resolution Order.

It is commonly used when a child class wants to extend a parent's behavior instead of replacing it completely.

### Example

```python
class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    def show(self):
        super().show()
        print("Child method")


obj = Child()
obj.show()
```

**Output:**

```text
Parent method
Child method
```

### Using `super()` with `__init__()`

```python
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


employee = Employee("Moin", 30000)

print(employee.name)
print(employee.salary)
```

**Output:**

```text
Moin
30000
```

The child class reuses the parent class's initialization logic and adds a `salary` attribute.

## 11. Parent and Child Class Attributes

A child class can access inherited attributes and methods, subject to normal Python attribute lookup and visibility conventions.

### Example

```python
class Person:
    category = "Human"

    def __init__(self, name):
        self.name = name


class Employee(Person):
    def display(self):
        print(self.name)
        print(self.category)


employee = Employee("Moin")
employee.display()
```

**Output:**

```text
Moin
Human
```

Here:

- `category` is a class attribute defined in `Person`.
- `name` is an instance attribute initialized by `Person`.
- `Employee` accesses both through inheritance.

Python does not enforce Java-style private or protected access modifiers. A single leading underscore is commonly used to indicate that an attribute is intended for internal use.

## 12. Practical Example: Employee Management

Inheritance can help represent different types of employees while sharing common properties and behavior.

```python
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


class DevOpsEngineer(Employee):
    def deploy_application(self):
        print("Deploying application")


class Developer(Employee):
    def write_code(self):
        print("Writing code")


devops = DevOpsEngineer("Moin", 101)
developer = Developer("Ayaan", 102)

devops.display_details()
devops.deploy_application()

developer.display_details()
developer.write_code()
```

**Output:**

```text
Name: Moin
Employee ID: 101
Deploying application
Name: Ayaan
Employee ID: 102
Writing code
```

### Explanation

- `Employee` contains common employee information.
- `DevOpsEngineer` inherits the common employee functionality and adds deployment behavior.
- `Developer` inherits the same functionality and adds coding behavior.

This avoids duplicating common attributes and methods.

## 13. Advantages of Inheritance

Inheritance provides several benefits:

- **Code reusability:** Common logic can be defined once in a parent class.
- **Reduced duplication:** Child classes can reuse existing implementations.
- **Extensibility:** Child classes can add new attributes and methods.
- **Customization:** Method overriding allows specialized behavior.
- **Maintainability:** Shared functionality can be updated in one place.
- **Logical organization:** Related classes can be structured into hierarchies.

## 14. Limitations of Inheritance

Inheritance is useful, but excessive use can make code difficult to maintain.

Potential problems include:

- Deep inheritance chains can be difficult to understand.
- Changes in a parent class can affect child classes.
- Multiple inheritance can make method resolution harder to follow.
- Unrelated classes may become tightly coupled through inappropriate inheritance.

Use inheritance when there is a meaningful **is-a** relationship.

For example:

- A `Dog` is an `Animal`.
- A `DevOpsEngineer` is an `Employee`.

If one object merely uses another object, composition may be more appropriate.

For example, a `Car` has an `Engine`; a car is not an engine.

## 15. Inheritance vs Composition

| Feature | Inheritance | Composition |
|---|---|---|
| Relationship | Is-a | Has-a |
| Code reuse | Inherits attributes and methods | Reuses another object's functionality |
| Coupling | Can create tighter coupling between classes | Often allows more flexible component replacement |
| Example | `Dog(Animal)` | `Car` contains an `Engine` object |
| Best suited for | Genuine class hierarchies | Combining independent components |

### Composition Example

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start()
```

**Output:**

```text
Engine started
Car started
```

The `Car` class uses an `Engine` object rather than inheriting from `Engine`.

## 16. Best Practices

- Use meaningful class and method names.
- Keep classes focused on related responsibilities.
- Use inheritance only when the relationship makes sense.
- Use `super()` when extending parent class behavior.
- Avoid unnecessarily deep inheritance hierarchies.
- Understand Python's Method Resolution Order when using multiple inheritance.
- Prefer composition when objects need to combine independent functionality.
- Document methods and classes when their purpose is not obvious.

## 17. Summary

Classes and inheritance are important concepts in Python's Object-Oriented Programming model.

- A **class** defines a blueprint for creating objects.
- An **object** is an instance of a class.
- `__init__()` initializes an object's attributes.
- `self` refers to the current instance.
- **Inheritance** allows one class to reuse functionality from another.
- **Method overriding** lets a child class customize inherited behavior.
- `super()` provides access to methods according to the inheritance hierarchy.
- Python supports single, multiple, multilevel, hierarchical, and hybrid inheritance.
- **Composition** is an alternative when one object contains or uses another object.

Understanding these concepts helps developers write reusable, organized, and maintainable Python applications.
