
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





