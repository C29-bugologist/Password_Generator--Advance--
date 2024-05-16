import string
import random #imported the random function 
print("----------Pass_Word_Genrator----------\n\n")
num = int(input("Enter the Lenght Of Password in Number: \n "))
complexicity = int(input("Select the Level Conmplexity of your program\n 1.Simple pin \n 2.Numbers and Letters \n 3.All printable Character\n Enter 4 to Exit\n   Enter no. :  "))
All_character = list(string.printable)
_ABCD_ = list(string.ascii_letters)
_numbers_ = list(range(0,9))
Number_Letter = _ABCD_ + _numbers_
while True: 
    if complexicity == 1:
        print(f"Your {num} Character passcode is ")
        print("".join(random.sample(_numbers_,num)))
    elif complexicity == 2:  
        print(f"Your {num} Character password is")
        print("".join(random.sample(Number_Letter,num)))
    elif complexicity == 3:  
        print(f"Your {num} Character password is ")
        print("".join(random.sample(All_character,num)))
    else:
        print("ERROR**plese enter either 6 or 4**")
        #Used if else statement so a user can only generate 6 digits or 4 digit code and we can give an error message