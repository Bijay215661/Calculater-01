again =True
# Mathmetical types
ad =  "1"
sb = "2"
mul = "3"
#print function
print(ad, "Addition")
print(sb, "Subraction")
print(mul,"Multiplication")
choise = input("Enter your chpoise : ")


# This line of code is for the addition

if choise == ad:
    big_number = int(input("Enter the first number to add: "))
    second_number = int(input("Enter the Second numbe: "))

    total_add = big_number +  second_number
    print("This is the added value: ", total_add)
# this one is for the subraction
elif choise == sb:
    fst_bg_number = int(input("Enter the first large number: "))
    sc_number = int(input("Enter the second number: "))

    sub_total = fst_bg_number - sc_number
    print("This is the subracted number: ", sub_total)

#This line of code is for multiplay
elif choise == mul:
    first_multi = int(input("Enter the first number: "))
    second_multi = int(input("Enter the Second numbe: "))

    total_multipal = first_multi *  second_multi
    print("This is the multiplyed value: ", total_multipal)


# This the continue again code
continue_again = input("Do you want to Contunue y/n: ")
if continue_again == "n":
    again = False
#while of the repearting
while again == True:
    # Mathmetical types
    ad =  "1"
    sb = "2"
    mul ="3"
    #print function
    print(ad, "Addition")
    print(sb, "Subraction")
    print(mul, "Multiplication")
    choise = input("Enter your chpoise : ")

    # This line of code is for the addition
    if choise == ad:
        big_number = int(input("Enter the first number to add: "))
        second_number = int(input("Enter the Second numbe: "))

        total_add = big_number +  second_number
        print("This is the added value: ", total_add)
    # this one is for the subraction
    elif choise == sb:
        fst_bg_number = int(input("Enter the first large number: "))
        sc_number = int(input("Enter the second number: "))

        sub_total = fst_bg_number - sc_number
        print("This is the subracted number: ", sub_total)
    #This line of code is for multiplay
    elif choise == mul:
        first_multi = int(input("Enter the first number: "))
        second_multi = int(input("Enter the Second numbe: "))
        total_multipal = first_multi *  second_multi
        print("This is the multiplyed value: ", total_multipal)    
    
    # This the continue again code
    continue_again = input("Do you want to Contunue y/n: ")
    if continue_again == "n":
        again = False

    
