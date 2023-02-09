language = input("What language do you prefer: ")
name = input("Name:  ")
gender = input("Gender: ")
location = input("Address: ")
independence = input("Are you able to work independently (Y/N): ")
education = input("Highest form of education you hold: ")

schedule = { "Monday": "NA", "Tuesday": "NA", "Wednesday": "NA", "Thursday": "NA", "Friday": "NA"}
# NA refers to not available on the day

days_of_the_week = input("Days of the week you are available: ")
print("Type in Mon/Tue/Wed/Thu/Fri. Separate them with a comma. For example, Mon, Tues")
available_days = []

for i in range(len(days_of_the_week)):
    if days_of_the_week[i] == ",":
        available_days.append(days_of_the_week[:i])

print("Please write in 24 hours format, for example: 0800-2000")    
for available_day in available_days:
    avail_time_on_that_day = input("Available time on {available_day}: ")
    days_of_the_week[available_days] = avail_time_on_that_day

print("Thank you for the information. Now, please tell us about yourself and we will generate a resume for you shortly.")

