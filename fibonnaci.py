n1 = 0
n2 = 1
n3 = 0

inputNum = int(input('How many numbers would you like to generate? '))

for x in range(inputNum):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
