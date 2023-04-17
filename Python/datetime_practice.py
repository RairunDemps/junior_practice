from datetime import datetime

date_test = datetime(2022, 10, 22)
print("Date without time", date_test)

datetime_test = datetime(2022, 10, 22, 6, 2, 32, 5456)
print("Datetime", datetime_test)

mindatetime = datetime.min
print("Min DateTime supported", mindatetime)

maxdatetime = datetime.max
print("Max DateTime supported", maxdatetime)

now = datetime.now()
print(f"Day: {now.day}, Month: {now.month}, Year: {now.year}, " \
      f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")

print("Today's date using now() method:", now)
today = datetime.today()
print("Today's date using today() method:", today)

date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)

date_time = datetime.fromordinal(737994)
print("Datetime from ordinal:", date_time)
