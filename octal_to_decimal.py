# ###############################
# name: DHEERAJ KUMAR SHRIVASTVA
# roll no: 21106
# ###############################

def oct_to_dec(number):
    dec = 0
    n = len(number)
    for i in number:
        dec += int(i)*8**(n-1)
        n -= 1
    return dec


print("\nwelcome to Octal to decimal conversion.")
oct = [0,1,2,3,4,5,6,7]

while input("\nDo you Want to convert octal to decimal: 'y' or 'n' ? ") == 'y':
    num = input("\nEnter Octal value : ")
    flag = 1
    for i in num:
        if i not in oct:
            
            flag = 0
    # main
    if flag == 1:
        if int(num) > 1:
            print(f"decimal conversion of Octal {num} is : ({oct_to_dec(num)})\n")
        else:
            print("I have't written the code for that only value > 1 \n")
    else:
        print(f"'{num}' is not a Hexadecimal number. Try again.")
print("GoodBye!!")
    