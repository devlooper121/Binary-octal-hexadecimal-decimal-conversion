# ###############################
# name: DHEERAJ KUMAR SHRIVASTVA
# Hexadecimal to binary converter
# ###############################

def hex_to_dec(number):
    dec = 0
    n = len(number)
    for i in number:
        if i == 'A' or i == 'a':
            i = 10
        elif i == 'B' or i == 'b':
            i = 11
        elif i == 'C' or i == 'c':
            i = 12
        elif i == 'D' or i == 'd':
            i = 13
        elif i == 'E' or i == 'e':
            i = 14
        elif i == 'F' or i == 'f':
            i = 15
        dec += int(i)*16**(n-1)
        n -= 1
    return dec

def dec_to_binary(number):
    binary = ''
    while number >= 1:
        if number % 2 == 0:
            binary += '0'
            number /= 2
        else:
            binary += '1'
            number =(number- 1)/2
    return binary[::-1]


print("\nwelcome to Hexadecimal to binary conversion.")
hex = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','A','B','C','D','E','F']


while input("\nDo you Want to convert Hexadecimal to Binary: 'y' or 'n' ? ") == 'y':
    num = input("\nEnter any positive Hexadecimal value : ")
    # for only hexadecimal input
    flag = 1
    for i in num:
        if i in hex:
            flag = 0
    
    # main
    if flag == 1:
        decimal = int(hex_to_dec(num))
        print(f"Binary conversion of Hexadecimal {num} is : ({dec_to_binary(decimal)})\n")
    else:
        print(f"'{num}' is not a hexadecimal number. Try again.")    
print("GoodBye!!")
    