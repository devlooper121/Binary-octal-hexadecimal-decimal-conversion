# ###############################
# name: DHEERAJ KUMAR SHRIVASTVA
# Decimal to binary converter
# ###############################

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

# def decimal_to_bin(number):
#     binary = '0.'
#     while number < 1:
#         number *= 2
#         if number > 1:
#             binary += '1'
#             number %=1
#         else:
#             binary += '0'
#     return binary

print("\nwelcome to Decimal to binary conversion.")
while input("Do you Want to convert decimal to binary: 'y' or 'n' ? ") == 'y':
    
    num = int(input("Enter any positive decimal number : "))
    if num > 1:
        print(f"Binary conversion of {num} : ({dec_to_binary(num)})\n")
    else:
        print(f"plese use only positive integers\n")