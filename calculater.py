ad =  "1"

sb = 2

print(ad, "Addition")
print(sb, "Subraction")
choise = input("Enter your chpoise : ")


 
if choise == ad:
    big_number = int(input("Enter the first number to add: "))
    second_number = int(input("Enter the Second numbe: "))

    total_add = big_number +  second_number
    print("This is the added value: ", total_add)

elif choise == sb:
    fst_bg_number = int(input("Enter the first large number: "))
    sc_number = int(input("Enter the second number: "))

    sub_total = fst_bg_number - sc_number
    print("This is the subracted number: ", sub_total)

    
