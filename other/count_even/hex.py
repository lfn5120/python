# This is the code for a Hexadecimal Calculator, in which it converges from Hexadecimal to Integers, it has a system that takes the brute input,
# makes it into a list, and inverts, so that the hexToDec function can follow an order that takes the base 16 as an increasing subject and 
# facilitates the processing of the data.
# It also takes into account that the user might not input valid data and so it simply returns 'None' if one or more characters are not listed in 
# the dictionary.
# It also contains a non-stop way of working that makes it easier for the user to calculate multiple values and only stops if the user asks to.




#declare
dict ={
    'O' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
    'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15
}
def hexToDec(self):
    ans = 0
    i = 0
    l = len(self)

    while i < l:
        if str(self[i]) not in dict:
            ans = 'None'
            break

        ans += dict[str(self[i])]*pow(16, i)
        i+= 1
    return ans

#format
print('''
.
.
.                                  HEXADECIMAL CALCULATOR
.     
.                       ENTER YOUR DESIRED HEXADECIMAL NUMBER AND I WILL
.                               CONVERT IT TO ITS INTEGER DECIMAL
.                                    [ TYPE 'STOP' TO END]
.
.
      ''')

while True:
    #calculate
    hex = input('In: ')
    if hex in ['stop','Stop','STOP']:
        print('Thank you for your preference, have a good one!')
        break
    hexlist = list(hex)
    hexlist.reverse()
    res = hexToDec(hexlist)

    #display
    print(f'Out: {res}')
    print('''
.
        ''')





