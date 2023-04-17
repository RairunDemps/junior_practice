import random


numbers = [1, 2, 3, 4, 5, 6]
print("Random choice from list:", random.choice(numbers))

string = "strive"
print("Random choice from string:", random.choice(string))

print("A random number from range is", random.randrange(20, 50, 3))


print("A random number between 0 and 1 is :", random.random())
random.seed(5)
print("The mapped random number with 5 is :", random.random())
random.seed(7)
print("The mapped random number with 7 is :", random.random())
random.seed(5)
print("The mapped random number with 5 is :", random.random())
random.seed(7)
print("The mapped random number with 7 is :", random.random())
random.seed()

sample_list = ['A', 'B', 'C', 'D', 'E']
print("Original list:", sample_list)
random.shuffle(sample_list)
print("Shuffled one time list:", sample_list)
random.shuffle(sample_list)
print("Shuffled second time list:", sample_list)

print("The random floating point number between 10 and 30 is:", random.uniform(10,30))
