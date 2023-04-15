# This program calculates and displays the travel expenses and remaining balance
    # 06-04-2023
    # CTI-110 P2HW1 - Travel Expense
    # Augustine Anquandah
print("This program calculates and displays travel expenses")
budget = float(input("Enter your budget : "))   
destination = input("Enter your destination : ")    
gas_expenses = float(input("How much you will spend on gas : "))    
accomodation = float(input("Approximately how much you need for accomodation ? : "))    
food_expenses = float(input("Last, how much do you need for food? : "))     
remaining_balance = budget - gas_expenses - accomodation - food_expenses    
print("---------Travel expenses-----------------")
print("Location :       " + destination)
print("Initial budget : " + str(budget))
print("Fuel :           " + str(gas_expenses))
print("Accomodation :   " + str(accomodation))
print("Food :           " + str(food_expenses))
print("--------------------------------------------")
print()
print("Remaining balance : " + str(remaining_balance))