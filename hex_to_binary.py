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
while input("\nDo you Want to convert Hexadecimal to Binary: 'y' or 'n' ? ") == 'y':
    num = input("\nEnter Hexadecimal value : ")
    decimal = int(hex_to_dec(num))
    print(f"Binary conversion of Hexadecimal {num} is : ({dec_to_binary(decimal)})\n")
    
print("GoodBye!!")
    