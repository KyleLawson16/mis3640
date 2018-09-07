import time

epoch_time = time.time()
sec_per_day = 60 * 60 * 24
total_days = epoch_time // sec_per_day
years = round(total_days // 365)
days = round(total_days % 365)
hours = round((epoch_time % sec_per_day) // 3600)
minutes = round(((epoch_time % sec_per_day) % 3600) // 60)
seconds = round((((epoch_time % sec_per_day) % 3600) % 60))
print(f'It has been {years} years, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds since the epoch.')
