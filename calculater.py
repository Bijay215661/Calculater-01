again =True

# Mathmetical types
options = {
    "add":"1", 
    "sub":"2",
    "mul":"3",
    "div":"4"
}


#print function
print(options["add"], "Addition")
print(options["sub"], "Subraction")
print(options["mul"],"Multiplication")
print(options["div"], "Division")
choise = input("Enter your choise : ")


# This line of code is for the addition

if choise == options["add"]:
    print("Addition")
    big_number = int(input("Enter the first number to add: "))
    second_number = int(input("Enter the Second numbe: "))

    total_add = big_number +  second_number
    print("This is the added value: ", total_add)
# this one is for the subraction
elif choise == options["sub"]:
    print("Subraction")
    fst_bg_number = int(input("Enter the first large number: "))
    sc_number = int(input("Enter the second number: "))

    sub_total = fst_bg_number - sc_number
    print("This is the subracted number: ", sub_total)

#This line of code is for multiplay
elif choise == options["mul"]:
    print("Multiplication")
    first_multi = int(input("Enter the first number: "))
    second_multi = int(input("Enter the Second numbe: "))

    total_multipal = first_multi *  second_multi
    print("This is the multiplyed value: ", total_multipal)

#This line of code is for the Division
elif choise == options["div"]:
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
    options={"add": "1",
            "sub":"2",
            "mul": "3",
            "div":"4"
            
            }
    #print function
    print(options["add"], "Addition")
    print(options["sub"], "Subraction")
    print(options["mul"], "Multiplication")
    print(options["div"], "Division")
    choise = input("Enter your chpoise : ")

    # This line of code is for the addition
    if choise == options["add"]:
        print("Addition")
        big_number = int(input("Enter the first number to add: "))
        second_number = int(input("Enter the Second numbe: "))

        total_add = big_number +  second_number
        print("This is the added value: ", total_add)
    # this one is for the subraction
    elif choise == options["sub"]:
        print("Subraction")
        fst_bg_number = int(input("Enter the first large number: "))
        sc_number = int(input("Enter the second number: "))

        sub_total = fst_bg_number - sc_number
        print("This is the subracted number: ", sub_total)
    #This line of code is for multiplay
    elif choise == options["mul"]:
        print("Multiplication")
        first_multi = int(input("Enter the first number: "))
        second_multi = int(input("Enter the Second numbe: "))
        total_multipal = first_multi *  second_multi
        print("This is the multiplyed value: ", total_multipal)

    #This line of code is for the Division
    elif choise == options["div"]:
        print("Division")
        first_division = int(input("Enter the first division number: "))
        second_division = int(input("Enter the divid numbe: "))

        total_division = first_division /  second_division
        print("This is the Divided value: ", total_division)    
    
    # This the continue again code
    continue_again = input("Do you want to Contunue y/n: ")
    if continue_again == "n":
        again = False

    
