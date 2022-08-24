# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

def what_season():     
    winter = ('Dec','Jan','Feb','Mar')
    spring = ('Mar','Apr','May','Jun')
    summer = ('Jun','Jul','Aug','Sep')
    fall = ('Sep','Oct','Nov','Dec')

    month = input('Enter the month of the year (Jan - Dec): ').capitalize()
    day = int(input('Enter the day of the month: '))

    # Winter: Dec 21 - Mar 19
    if month in winter:
        # Jan and Feb
        if month == 'Jan' or month == 'Feb':
            print(f'{month} {day} is in winter')
        # Dec
        elif month == 'Dec' and 21 <= day <= 31:
            print(f'{month} {day} is in winter')
        # Mar
        elif month == 'Mar' and 1 <= day <= 19:
            print(f'{month} {day} is in winter')

    # Spring: Mar 20 - Jun 20
    if month in spring:
        # Apr and May
        if month == 'Apr' or month == 'May':
            print(f'{month} {day} is in spring')
        # Mar
        elif month == 'Mar' and 20 <= day <= 31:
            print(f'{month} {day} is in spring')
        # Jun
        elif month == 'Jun' and 1 <= day <= 20:
            print(f'{month} {day} is in spring')

    # Summer: Jun 21 - Sep 21
    if month in summer:
        # Jul and Aug
        if month == 'Jul' or month == 'Aug':
            print(f'{month} {day} is in summer')
        # Jun
        elif month == 'Jun' and 21 <= day <= 30:
            print(f'{month} {day} is in summer')
        # Sep
        elif month == 'Sep' and 1 <= day <= 21:
            print(f'{month} {day} is in summer')

    # Fall: Sep 22 - Dec 20
    if month in fall:
        #  Oct and Nov
        if month == 'Oct' or month == 'Nov':
            print(f'{month} {day} is in fall')
        # Sep
        if month == 'Sep' and 22 <= day <= 30:
            print(f'{month} {day} is in fall')
        # Dec
        if month == 'Dec' and 1 <= day <= 20:
            print(f'{month} {day} is in fall')

what_season()

# WARNING: There is no validation for the date inputted.