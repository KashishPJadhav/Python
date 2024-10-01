from datetime import datetime
now=datetime.now()
print("Current date and time is : ",now)

date_obj=datetime(2024,10,1,12,20)
print("Date time object created : ",date_obj)

#converting string to datetime
date_str='2024-10-1  12:22:30'
date_form=datetime.strptime(date_str, '%Y-%m-%d  %H:%M:%S')
print("String to Date-time : ",date_form)

form_date=date_obj.strftime('%Y-%m-%d %H:%M:%S')
print("Date object to string : ",form_date)

time_diff=datetime.now()-date_obj
print("Time difference : ",time_diff)
