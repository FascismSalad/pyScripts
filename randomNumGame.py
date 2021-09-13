import random

def main():
    check = 'yes'
    while check == 'yes' or check == 'y':

        randomNum = random.randint(1,100)
        guessNum = 0

        while randomNum != guessNum:
            guessNum = int(input('Make a guess: '))

            if guessNum > randomNum:
                print('Lower')

            elif guessNum < randomNum:
                print('Higher')

            elif guessNum == randomNum:
                print('Correct!')

            else:
                print('Error')


     userInput = input('Would you like to play again? y/n')

    print('Thank you for playing!')




main()
