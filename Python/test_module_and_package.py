import my_module
from my_module import module_dict
from my_package import my_module1

name = "Roland"
my_module.greeting(name)
print(module_dict)

name1 = "Dylan"
my_module1.greeting(name1)
print(my_module1.module_dict)
