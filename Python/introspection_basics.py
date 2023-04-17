# dir
number = [12]
print(dir(number))

# getattr
class Person:
  name = 'Sheeran'

class Student(Person):
  marks = 88

student = Student()
name = getattr(student, 'name')
marks = getattr(student, 'marks')
print(name, marks)

# id
print("The id of student is", id(student))

# hasattr
print("student has age attribute:", hasattr(student, "age"))
print("student has name attribute:", hasattr(student, "name"))

# issubclass
print("Student is subclass of Person:", issubclass(Student, Person))

# isinstance
print("student is instance of Student:", isinstance(student, Student))

# locals
print(locals())

# globals
print(globals())
