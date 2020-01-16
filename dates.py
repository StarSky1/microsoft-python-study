# to get current date and time
# we need to use the datetime library
from datetime import datetime,timedelta

current_date=datetime.now()
# the now function returns a datetime object
print('Today is: '+str(current_date))

# timedelta is used to define a period of time
one_day=timedelta(days=1)
yesterday=current_date-one_day
print('Yesterday was: '+str(yesterday))

one_week=timedelta(weeks=1)
last_week=current_date-one_week
print('last week was: '+str(last_week))

print('Day: '+str(current_date.day))
print('Month: '+str(current_date.month))
print('Year: '+str(current_date.year))
print('Hour: '+str(current_date.hour))
print('Minute: '+str(current_date.minute))
print('Second: '+str(current_date.second))

birthday=input('When is your birthday (dd/mm/yyyy)?')
birthday_date=datetime.strptime(birthday,'%d/%m/%Y')
print('Birthday: '+str(birthday_date))

one_day=timedelta(days=1)
birthday_eve=birthday_date-one_day
print('Day before birthday: '+str(birthday_eve))