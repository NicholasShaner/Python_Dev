import random

answer = 'y'

while answer == 'y':
    lw_b = int(input('Enter lower bounds: '))
    up_b = int(input('Enter upper bounds: '))
    while lw_b > up_b:
        print('Lower bounds cannot be higher than upper bounds')
        lw_b = int(input('Enter lower bounds: '))
        up_b = int(input('Enter upper bounds: '))
    else:
        rand_num = random.randint(lw_b, up_b)
        while lw_b < up_b:
            guess = int(input(f'Enter number between {lw_b} and {up_b}: '))
            if guess < rand_num:
                print('Not Quite Enough.')
            elif guess > rand_num:
                print('Woah! Too High.')
            elif guess == rand_num:
                print('You Got It!!', end=' ')
                print('Good Game!')
                answer = input("Play again? y/n? ").lower()
                if answer not in ('y', 'n'):
                    print('I did not get that.')
                    answer = input("Play again? y/n? ").lower()
                break
else:
    while answer == 'n':
        print('Very well! Come back again soon! Goodbye')
        break
