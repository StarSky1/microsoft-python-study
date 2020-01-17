# A student makes honour roll if their average is >=85
# and their lowest grade is not below 70

# I check to see if the requirements for honour roll are met 
gpa=float(input('What was your Grade Point Average?'))
lowest_grade=input('What was your lowest grade?')
lowest_grade=float(lowest_grade)

if gpa>= .85 and lowest_grade >=.70:
    honour_roll = True
else:
    honour_roll = False        

# Somewhere later in your code if you need to check if students is
# on honour roll,all I need to do is check the boolean variable
# I set earlier in my code.    
if honour_roll:
    print('You made the honour roll.')