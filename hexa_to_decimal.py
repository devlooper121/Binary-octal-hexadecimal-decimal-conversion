# ###############################
# name: DHEERAJ KUMAR SHRIVASTVA
# roll no: 21106
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


print("\nwelcome to Hexadecimal to decimal conversion.")
hex = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','A','B','C','D','E','F']

while input("\nDo you Want to convert Hexadecimal to Decimal: 'y' or 'n' ? ") == 'y':
    num = input("\nEnter Hexadecimal value : ")
    flag = 1
    for i in num:
        if i not in hex:
            
            flag = 0
    # main
    if flag == 1:
        print(f"decimal conversion of Hexadecimal {num} is : ({hex_to_dec(num)})\n")
    else:
        print(f"'{num}' is not a Hexadecimal number. Try again.")

print("GoodBye!!")
    