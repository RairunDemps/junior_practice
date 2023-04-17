from datetime import datetime, timedelta, date

now_time = datetime.now()
print("initial_date", str(now_time))

future_date_after_two_years = now_time + timedelta(days=730)
future_date_after_two_days = now_time + timedelta(days=2)
print("future_date_after_two_years:", str(future_date_after_two_years))
print("future_date_after_two_days:", str(future_date_after_two_days))

past_date_before_2years = now_time - timedelta(days=730)
past_date_before_2hours = now_time - timedelta(hours=2)
print("past_date_before_2years", str(past_date_before_2years))
print("past_date_before_2hours", str(past_date_before_2hours))

new_time = now_time + timedelta(days=2)
print("new_time", str(new_time))
print("Time difference:", str(new_time - now_time))

today = date.today()
three_days_ago = today - timedelta(days=3)
print("Today:", today)
print("Three days ago:", three_days_ago)
