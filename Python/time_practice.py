import time

seconds = time.time()
print("Seconds since epoch =", seconds)

local_time = time.ctime(seconds)
print("Local time:", local_time)

sleep_time = 1
print("Printed immediately.")
time.sleep(sleep_time)
print(f"Printed after {sleep_time} seconds")

result = time.localtime(seconds)
print(f"Result: {result}\nyear: {result.tm_year}, tm_hour: {result.tm_hour}")

result = time.gmtime(seconds)
print(f"result: {result}\nyear: {result.tm_year}, tm_hour: {result.tm_hour}")

time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
seconds = time.mktime(time_tuple)
print(f"Seconds from time_tuple {time_tuple} is {seconds}")

result = time.asctime(time_tuple)
print(f"Datetime string from time_tuple {time_tuple} is {result}")

named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(f"Datetime formatted string from named_tuple {named_tuple} is {time_string}")

time_string = "14 July, 2023"
result = time.strptime(time_string, "%d %B, %Y")

print(f"struct_time from time_string {time_string} is {result}")
