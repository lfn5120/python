def Factorial(i):
    s = 1
    if type(i) is not int:
        return print('None')
    elif i < 0:
        return print('None')
    elif i == 0:
        return print('The Answer is 1')
    while i > 0:
        s *= i
        i -= 1
    return s

num = int(input('Please Enter a Number and you will be provided with its respective Factorial: '))

print(Factorial(num))
