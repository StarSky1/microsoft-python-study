first_name='Yang';
last_name='Jing';
# first_name=input('Please enter your first name:')
# last_name=input('Please enter your last name:')
# print(first_name+' '+last_name);
print('Hello, '+first_name.capitalize()+' '+last_name.capitalize())
output='Hello, '+first_name+' '+last_name
output1='Hello, {} {}'.format(first_name,last_name)
output2='Hello, {0} {1}'.format(first_name,last_name)
# Only available in Python 3
output3=f'Hello, {first_name} {last_name}'
print(output,output1,output2,output3)