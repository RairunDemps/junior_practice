# Iterator
string = "BFG"
ch_iterator = iter(string)
 
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))


# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(next(x), next(x), next(x))
