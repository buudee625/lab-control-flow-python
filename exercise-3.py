# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

def doggo_age():
    try:
        age = int(input('Input a dog\'s age in human years: '))
        if 0 < age <= 2:
            age *= 10
            print(f'The dog\'s age in dog years is {age}')
        elif 2 < age < 30: 
            age = 20 + (age - 2) * 7
            print(f'The dog\'s age in dog years is {age}')
        elif age >= 31:
            print('The world\'s verified oldest dog Bluey lived 29 years, 5 months. RIP good doggo.')
        else:
            print('Negative age doesn\'t make much sense does it dawg?')
    except:
        print('You didn\'t enter a number dawg.')

doggo_age()