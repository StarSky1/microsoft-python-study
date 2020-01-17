# import the datetime class form datetime library
from datetime import datetime
# Print the current time and task name 
def print_time(task_name):
    print(task_name)
    # now I don't need the extra datetime prefix
    print(datetime.now())
    print()

first_name='Susan'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')

def get_initial(name):
    initial=name[0:1]
    return initial

first_name=input('enter your first name:')
first_name_initial=get_initial(first_name)
last_name=input('enter your last name:')
last_name_initial=get_initial(last_name)

print('Your initials are: {0}{1}'.format(first_name_initial,last_name_initial))
print_time('test completed')