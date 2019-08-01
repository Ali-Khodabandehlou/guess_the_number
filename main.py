import random


def create_rand_num(hardiness):
    num = 10 **hardiness
    num = random.randint(1, num)
    return num


def play_guess(num):
    answer = False
    for i in range(0, 10):
        guess = input('\nRemaining guesses: ' + str((10 - i)) + '\nEnter your guess:')
        answer = check_guess(int(guess), num)
        if answer == True:
            print('\nNumber of guesses: ' + str((i + 1)))
            break
    
def check_guess(guess, num):
    if guess < num:
        print('\nThe number is bigger!')
        return False
    elif guess > num:
        print('\nThe number is smaller!')
        return False
    elif guess == num:
        print('\nCongradulations!\nYou guessed right!\n\nThe number was: ' + str(guess))
        return True
    else:
        print('\nAttention: Unsupported entry!')
        return False


def main():
    print('\nWelcome to the "guess the number" game!')
    
    while True:
        hardiness = input('\nSelect the difficulty of the game:(1: easy, 2: rough 3: badass)')
        try:
            val = int(hardiness)
            number = create_rand_num(val)
            play_guess(number)
        except ValueError:
            print('\nPlease enter a number')
            continue

        _continue = input('\nDo you want to play again?(y/n)').lower()
        if _continue != 'y':
            input('\nThat was fun playing with you!\nHope to see you again :)')
            break


if __name__ == '__main__':
    main()