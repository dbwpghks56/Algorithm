import sys

monthDays = sys.stdin.readline()
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
totalDay = 365

manmonth, mantime = monthDays.split(',')

month, day = manmonth.split()
year, time = mantime.split()
hour, minute = time.split(":")

hour = int(hour)
minute = int(minute)
year = int(year)
day = int(day)

if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
    days[1] = 29
    totalDay += 1

monthIndex = months.index(month) +1

elapsed_days = sum(days[:monthIndex - 1]) + day
day_progress = (elapsed_days / totalDay) * 100

total_minutes = totalDay * 24 * 60
elapsed_minutes = ((elapsed_days - 1) * 24 * 60) + (hour * 60) + minute
total_progress = (elapsed_minutes / total_minutes) * 100

# dayPer = (day / days[monthIndex -1]) * 100
# monthPer = (monthIndex / 12) * 100
# hourPer = (hour / 24) * 100
# minutePer = (minute / 60) * 100

print(total_progress)
