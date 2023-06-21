again =True
print("1234")
print("456")
print("34")
# Mathmetical types
ad =  '1'
sb = '2'
mul = '3'
dev = '4'

#print function
print(ad, "Addition")
print(sb, "Subraction")
print(mul,"Multiplication")
print(dev, "Division")
choise = input("Enter your choise : ")


# This line of code is for the addition

if choise == ad:
    print("Addition")
    big_number = int(input("Enter the first number to add: "))
    second_number = int(input("Enter the Second numbe: "))

    total_add = big_number +  second_number
    print("This is the added value: ", total_add)
# this one is for the subraction
elif choise == sb:
    print("Subraction")
    fst_bg_number = int(input("Enter the first large number: "))
    sc_number = int(input("Enter the second number: "))

    sub_total = fst_bg_number - sc_number
    print("This is the subracted number: ", sub_total)

#This line of code is for multiplay
elif choise == mul:
    print("Multiplication")
    first_multi = int(input("Enter the first number: "))
    second_multi = int(input("Enter the Second numbe: "))

    total_multipal = first_multi *  second_multi
    print("This is the multiplyed value: ", total_multipal)

#This line of code is for the Division
elif choise == dev:
    print("Division")
    first_division = int(input("Enter the first number: "))
    second_division = int(input("Enter the Second numbe: "))

    total_division = first_division /  second_division
    print("This is the Divided value: ", total_division)


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
    dev = "4"
    #print function
    print(ad, "Addition")
    print(sb, "Subraction")
    print(mul, "Multiplication")
    print(dev, "Division")
    choise = input("Enter your chpoise : ")

    # This line of code is for the addition
    if choise == ad:
        print("Addition")
        big_number = int(input("Enter the first number to add: "))
        second_number = int(input("Enter the Second numbe: "))

        total_add = big_number +  second_number
        print("This is the added value: ", total_add)
    # this one is for the subraction
    elif choise == sb:
        print("Subraction")
        fst_bg_number = int(input("Enter the first large number: "))
        sc_number = int(input("Enter the second number: "))

        sub_total = fst_bg_number - sc_number
        print("This is the subracted number: ", sub_total)
    #This line of code is for multiplay
    elif choise == mul:
        print("Multiplication")
        first_multi = int(input("Enter the first number: "))
        second_multi = int(input("Enter the Second numbe: "))
        total_multipal = first_multi *  second_multi
        print("This is the multiplyed value: ", total_multipal)

    #This line of code is for the Division
    elif choise == dev:
        print("Division")
        first_division = int(input("Enter the first division number: "))
        second_division = int(input("Enter the divid numbe: "))

        total_division = first_division /  second_division
        print("This is the Divided value: ", total_division)    
    
    # This the continue again code
    continue_again = input("Do you want to Contunue y/n: ")
    if continue_again == "n":
        again = False

    
