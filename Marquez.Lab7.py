#input
name = input("Name: ")
section = input("Section: ")
prelim = float(input("Prelim Grade: "))
midterm = float(input("Midterm Grade: "))
finals = float(input("Finals Grade: "))
final_grade = (prelim * .3333) + (midterm * .3333) + (finals * .3333)

#output

if final_grade < 40 or final_grade > 100:
    print("Invalid Grades Input")
    exit

elif final_grade <= 74:
    print(f"{final_grade:.0f} \n5.00 \nFailed")

elif final_grade >= 75 and final_grade <= 77:
    print(f"{final_grade:.0f} \n3.00 \nPassed")
    
elif final_grade >= 78 and final_grade <= 80:
    print(f"{final_grade:.0f} \n2.75 \nFair")
    
elif final_grade >= 81 and final_grade <=83:
    print(f"{final_grade:.0f} \n2.50 \nFairly Satisfactory")
    
elif final_grade >= 84 and final_grade <= 86:
    print(f"{final_grade:.0f} \n2.25 \nSatisfactory")

elif final_grade >= 87 and final_grade <= 89:
    print(f"{final_grade:.0f} \n2.00 \nGood")
    
elif final_grade >= 90 and final_grade <= 92:
    print(f"{final_grade:.0f} \n1.75 \nVery Good")

elif final_grade >= 93 and final_grade <= 95:
    print(f"{final_grade:.0f} \n1.50 \nSuperior")
    
elif final_grade >= 96 and final_grade <= 98:
    print(f"{final_grade:.0f} \n1.25 \nOutstanding")

elif final_grade >= 99 and final_grade <= 100:
    print(f"{final_grade:.0f} \n1.00 \nExcellent")


    