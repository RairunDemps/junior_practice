def change_m_to_l(func):
    def inner1(*args, **kwargs):
        print("Before execution")
        new_args = (x.replace("m", "l") for x in args)

        returned_value = func(*new_args, **kwargs)

        print("This is after function execution")

        return returned_value

    return inner1

@change_m_to_l
def print_string(name="Gamma"):
    print("Inside the function")
    print(name)
    
    return [x for x in range(0, 10, 2)]

print(print_string("Tama"))