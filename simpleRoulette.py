import random

def main():
    money = 100
    answer = 'y'

    while answer == 'y':


        betAmount = input('How much would you like to bet?: ')
        betType = input ('Enter your bet type: \nstraight \nzero \nodds \nevens \n5 way\n')



        if betType == 'straight':
            ball = print(random.randint(1,36))
            num = input('which number would you like to bet on between 1-36')

            if int(num) == ball:
                winAmount = int(betAmount) * 35
                money = money + winAmount
                print('You Win! You bet ', int(betAmount), ' and won ', winAmount, '. You now have ', money)

            elif num != ball:
                print('You lose')



        elif betType == 'zero':
            print('test')



        elif betTyoe == 'odds':
            print('test')

        elif betType == 'evens':
            print('test')

        elif betType == '5 way':
            print('test')

        else:
            print('Error, Something went wrong. Try Again')
            return

    answer = input('Would you like to bet again? y/n')

main()



#bet on single number, 35:1 odds
#bet on 0, 100:1 odds
#bet on odd, 1:1 odds
#bet on even, 1:1 odds
#bet on 5 different numbers, 1:2 odds
