class Person:

    def __init__(self, name: str) -> None:
        print("Person __init__ called")
        self._name = name

    def __call__(self) -> None:
        print(f"Just using __call__ from class {__class__.__name__}")

    def __str__(self) -> str:
        return f"Calling __str__ function from class {__class__.__name__}"

    def __repr__(self) -> str:
        return f"Calling __repr__ function from class {__class__.__name__}"

    def greet(self) -> None:
        print(f"Hello, my name is {self._name}")

class Worker(Person):

    def __init__(self, name: str, type: str) -> None:
        print("Worker __init__ called")
        super().__init__(name)
        self._type = type

    def greet(self) -> None:
        super().greet()
        print(f"I am {self._type} worker")

name = "Ace"
person = Person(name=name)
person.greet()
person()
print(person)
print(person.__repr__())

# worker_name = "Geats"
# type = "active"
# worker = Worker(name=worker_name, type=type)
# worker.greet()

# print(worker.__dict__)
# print(Worker.__dict__)
