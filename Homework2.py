"""
Class: CS230--Section 5
Name: Sanjana Sathiyavanthan
Date: 10.09.25
Description: This is a program that is a time zone comparison calculator that is based on the world clock meeting planner.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

# These are the constants for this assignment.
NEW_YORK_OFFSET = -5
LONDON_OFFSET = 1
TOKYO_OFFSET = 9
LOS_ANGELES_OFFSET = -8
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
DAY_MINUTES = HOURS_IN_DAY * MINUTES_IN_HOUR

# This is part 1 of the program which is supposed to display a table of corresponding times for two different cities that the user  selects
print("-------- City Time Zone Comparison Calculator --------") # this will match what the homework requires
print("Available cities: NEW YORK, LONDON, TOKYO, LOS ANGELES")
print("------------------------------------------------------")

# This will ask the user for the first city
city1 = input("Enter city 1: ").upper()
while not (city1 == "NEW YORK" or city1 == "LONDON" or city1 == "TOKYO" or city1 == "LOS ANGELES"):
    print("Invalid city. Please choose from NEW YORK, LONDON, TOKYO, LOS ANGELES.")
    city1 = input("Enter city 1: ").upper()

# This will ask the user for the second city
city2 = input("Enter city 2: ").upper()
while not (city2 == "NEW YORK" or city2 == "LONDON" or city2 == "TOKYO" or city2 == "LOS ANGELES"):
    print("Invalid target city. Please choose from NEW YORK, LONDON, TOKYO, LOS ANGELES.")
    city2 = input("Enter city 2: ").upper()

# This will match city names to different offsets that were provided.
if city1 == "NEW YORK":
    offset1 = NEW_YORK_OFFSET
elif city1 == "LONDON":
    offset1 = LONDON_OFFSET
elif city1 == "TOKYO":
    offset1 = TOKYO_OFFSET
else:
    offset1 = LOS_ANGELES_OFFSET

if city2 == "NEW YORK":
    offset2 = NEW_YORK_OFFSET
elif city2 == "LONDON":
    offset2 = LONDON_OFFSET
elif city2 == "TOKYO":
    offset2 = TOKYO_OFFSET
else:
    offset2 = LOS_ANGELES_OFFSET

# Prints the table based on what was entered
print("\n====== Time Zone Comparison ======")
print(f"{city1:<11} | {city2}")
print("-----------------------------------")

for hour in range(0, HOURS_IN_DAY):
    # the minutes that are past midnight
    city1_minutes = hour * MINUTES_IN_HOUR

    # calculates the time difference in minutes
    diff_hours = offset2 - offset1
    diff_minutes = diff_hours * MINUTES_IN_HOUR
    city2_minutes = city1_minutes + diff_minutes

    # checks if it is next or previous day
    note = ""
    if city2_minutes >= DAY_MINUTES:
        city2_minutes = city2_minutes % DAY_MINUTES
        note = " (next day)"
    elif city2_minutes < 0:
        city2_minutes = city2_minutes + DAY_MINUTES
        note = " (previous day)"

    # convert back to hours or minutes
    city1_hour = hour
    city2_hour = city2_minutes // MINUTES_IN_HOUR

    # this formats into the AM/PM
    if city1_hour == 0:    # this converts the first city hour into AM/PM
        city1_display = "12:00 AM"
    elif city1_hour < 12:
        city1_display = f"{city1_hour}:00 AM"
    elif city1_hour == 12:
        city1_display = "12:00 PM"
    else:
        city1_display = f"{city1_hour - 12}:00 PM"

    if city2_hour == 0:  # this convert the second city hour into AM/PM
        city2_display = "12:00 AM"
    elif city2_hour < 12:
        city2_display = f"{city2_hour}:00 AM"
    elif city2_hour == 12:
        city2_display = "12:00 PM"
    else:
        city2_display = f"{city2_hour - 12}:00 PM"

    # Print the formatted times
    print(f"{city1_display:<11} | {city2_display}{note}")

# This is part 2 which is supposed to display the ending time for a meeting given its start time, AM/PM, and duration (in  minutes).

print("\n-------- Meeting End Time Calculator --------") # all of this matches the format required for the homework
start_hour = int(input("Enter the hour that the meeting should start: "))
start_min = int(input("Enter the minutes after the hour that the meeting should start: "))
am_pm = input("Enter AM or PM: ").upper()
duration = int(input("Enter the duration of the meeting (in minutes): "))

# Converting the start time to 24-hour minutes so it can be easier to use
if am_pm == "PM" and start_hour != 12:
    start_hour += 12
if am_pm == "AM" and start_hour == 12:
    start_hour = 0

start_total = start_hour * MINUTES_IN_HOUR + start_min
end_total = start_total + duration

# Checking if this will be next day which is only if the meeting will end after midnight
next_day = ""
if end_total >= DAY_MINUTES:
    end_total = end_total % DAY_MINUTES
    next_day = " next day"

# Converting the time back to hour or minute
end_hour = end_total // MINUTES_IN_HOUR
end_min = end_total % MINUTES_IN_HOUR

# Formating this into AM/PM
if end_hour == 0:
    display_hour = 12
    am_pm = "AM"
elif end_hour < 12:
    display_hour = end_hour
    am_pm = "AM"
elif end_hour == 12:
    display_hour = 12
    am_pm = "PM"
else:
    display_hour = end_hour - 12
    am_pm = "PM"

# This will print the output of the meeting end time based on what the user had entered
print(f"Meeting will end at: {display_hour:02}:{end_min:02} {am_pm}{next_day}")
