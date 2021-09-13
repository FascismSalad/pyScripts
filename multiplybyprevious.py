def main():
    n = 2

    inputNum = int(input('How many numbers would you like to generate? '))

    for x in range(inputNum):
        n *= n
        print(n)

main()
