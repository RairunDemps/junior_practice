import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

# try:
#     linux_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('Linux linux_interaction() function was not executed')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')

# x = 10
# if x > 5:
#     raise Exception("x is bigger than 5")