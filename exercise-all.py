# --------------------------------------
# exercise-01
# --------------------------------------

# ch = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
# if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#     print(f'The letter {ch} is a vowel')
# else:
#     print(f'The letter {ch} is a consonant')

# --------------------------------------
# exercise-02
# --------------------------------------

# while True:
#     str = input('Please enter a word or phrase: ')
#     if str != 'quit':
#         print(f'What you entered is {len(str)} characters long.')
#         print('Enter "quit" to stop the program.')
#     else:
#         break

# --------------------------------------
# exercise-03 
# --------------------------------------

# try:
#     age = int(input('Input a dog\'s age in human years: '))
#     if 0 < age <= 2:
#         age *= 10
#         print(f'The dog\'s age in dog years is {age}')
#     elif 2 < age < 30: 
#         age = 20 + (age - 2) * 7
#         print(f'The dog\'s age in dog years is {age}')
#     elif age >= 31:
#         print('The world's verified oldest dog Bluey lived 29 years, 5 months. RIP good doggo.')
#     else:
#         print('Negative age doesn\'t make much sense does it dawg?')
# except:
#     print('You didn\'t enter a number dawg.')

# --------------------------------------
# exercise-04
# --------------------------------------
# ex4 = 1
# sides = []
# while ex4 < 4:
#     answer = input(f'Enter the lengths of the number {ex4} side of a triangle: ')
#     sides.append(answer)
#     ex4 += 1

# if len(set(sides)) == 1:
#     print(f'A triangle with sides of {sides[0]}, {sides[1]} & {sides[2]} is a equalateral triangle')
# elif len(set(sides)) == 2:
#     print(f'A triangle with sides of {sides[0]}, {sides[1]} & {sides[2]} is a isosceles triangle')
# elif len(set(sides)) == 3:
#     print(f'A triangle with sides of {sides[0]}, {sides[1]} & {sides[2]} is a scalene triangle')

# --------------------------------------
# exercise-05
# --------------------------------------
# i = 0
# total = 0
# fib1 = 0
# fib2 = 1

# while i <= 50:
#     print(f'term:{i} / number: {total}')
#     fib1 = fib2
#     fib2 = total
#     total = fib1 + fib2
#     i += 1 

# --------------------------------------
# exercise-06 What's the  Season?
# --------------------------------------

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