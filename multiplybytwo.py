def main():
    n = 1

    inputNum = int(input('How many numbers would you like to generate? '))

    for x in range(inputNum):
        n *= 2
        print(n)

main()
