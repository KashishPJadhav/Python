from datetime import datetime

# Getting the current datetime
today_day = datetime.now()  
print("Today's date and time is: ", today_day)

# Create a specific datetime
Newdate = datetime(2004, 4, 3, 14, 30, 29) 
print("Specific date and time is: ", Newdate)

Day = int(input("Enter the day: ")) 
Month = int(input("Enter the month: ")) 
Year = int(input("Enter the year: "))

date_object = datetime(Year, Month, Day) 
print("Entered date and time is: ", date_object)

# Convert string to datetime
dateTime_string = "2024-09-15 14:30:29"
StrToDateTime = datetime.strptime(dateTime_string, "%Y-%m-%d %H:%M:%S")
print("Converting string to datetime: ", StrToDateTime)

# Convert datetime to string
DateTimetostr = datetime.strftime(Newdate, "%Y-%m-%d %H:%M:%S")
print("Converting datetime to string: ", DateTimetostr)

# Difference between current date and specific date
dateDifference = today_day - date_object
print("The difference between current date and specific date: ", dateDifference)

total_days = dateDifference.days
years = total_days // 365
remaingDays = total_days % 365
total_months = remaingDays  // 30
print(years," years"," and ", total_months ," months",remaingDays," days")
