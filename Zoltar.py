import random
import time

# this program prompts the user to select a numbered option 1-3
# and based on the choice displays lucky numbers, fortune cookie advice, or tells the future
# it is based loosely on the boardwalk game Zoltar the Magnificent

# does the user want to keep playing? initial is true
zoltar = True


# function definitions
# function to look like Zoltar is thinking
def thinking():
    print('Hmm... Let me think about these things. Soon I will give an answer.')
    time.sleep(.5)
    for i in range(4):
        # tried  print('.',end='') but it waited the combined time and then displayed all dots at once
        print('.')
        time.sleep(.5)


# function to read a fortune or advice at random from a file depending on which is chosen
def fortune_advice(fname):
    all_lines = open(fname).read().splitlines()
    return random.choice(all_lines)


# this function returns six pairs of integers at random
# still working on the return value, need to do some research on how to better define this function in python
def lucky_numbers():
    print('Your Lucky numbers are: ', '\n')
    for i in range(5):
        x = random.randint(10, 99)
        print(x, end=' ')
    return random.randint(10, 99)


# this function will allow the user to make another choice from Zoltar
def again():
    i = ''
    while i != 'y' and i != 'n':
        print('\n', 'Would you like to play again?  y or n ')
        i = input()
        if i == str.lower('y'):
            print('Very well,')
            return i
        elif i == str.lower('n'):
            print('Goodbye then.')
            return i
        else:
            print('Please enter only y or n')


# begin output
while zoltar == True:
    print('Welcome. I am Zoltar the Magnificent. If you dare, you may seek my wisdom by selecting a choice below:')
    print('1 - Seek your fortune. But beware, you may not like what your future holds!')
    print('2 - Ask for my advice. It is up to you to decipher its grand meaning.')
    print('3 - Show my lucky numbers for today.')
    print('Please select 1, 2, or 3 and press the enter key...')

    # this will hold the user's selection
    valid_num = False
    while valid_num == False:
        my_int = input()

    # input validation
        try:
            if int(my_int) > 3 or int(my_int) < 1:
                print('Please enter only 1, 2, or 3')
            else:
                valid_num = True
                continue
        # if non numeric, ask again
        except ValueError:
            print('Please enter only 1, 2, or 3')

        print(my_int)

    # fortune seeker
    if int(my_int) == 1:
        thinking()
        print('You have chosen to have your fortune told to you. Zoltar says:', '\n')
        print(fortune_advice('advice_fortunes/fortune.txt'))
        again()

    # advice seeker
    elif int(my_int) == 2:
        thinking()
        print('You have chosen to seek advice. Zoltar says:', '\n')
        print(fortune_advice('advice_fortunes/advice.txt'))
        again()

    # lucky numbers
    else:
        thinking()
        print('You have chosen to reveal your lucky numbers. Zoltar says')
        print(lucky_numbers())
        again()