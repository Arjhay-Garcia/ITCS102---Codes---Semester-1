# Bank loan interest and Interest Rate Provider
# Loadn Engine Challenge

age = int(input("Enter your age: "))
is_employed = input("Are you currently employed? ")

if is_employed == "true" or "True" or "yes" or "Yes":
    is_employed = True
else:
    is_employed = False
    
credit_score = int(input("What's your Credit Score? "))
annual_income = float(input("what's your annual salary? "))
has_collateral = input("Do you have any Collateral? ")

if has_collateral == "true" or "True" or "yes" or "Yes":
    has_collateral = True
else:
    has_collateral = False
    

base_interest = float(0)


if age >= 21 and is_employed == True:
    print("\n\nUser is eligible\n")
    if credit_score >= 750: #tier1
        base_interest = 5
        if annual_income >= 100000:
            base_interest = 4.5
            print("You are a Tier 1 with Loyalty Discount. \nYour Base Interest Rate is", base_interest, "%")
        else:
            base_interest = 5
            print("You are a Tier 1. \nBase Interest Rate is", base_interest, "%")
    elif credit_score < 750 and has_collateral == False:
        base_interest = 8
        print("You are a Mid Tier 2. Your Base Interest Rate is", base_interest, "%")
        if 600 <= credit_score < 750 and has_collateral == True:
            base_interest = 7
            print("You are a High Tier 2. Your Base Interest Rate is", base_interest, "%")
        elif has_collateral == False and annual_income < 40000:
            base_interest = 9.5
            print("You are a Low Tier 2. Your Base Interest Rate is", base_interest, "%")
        else:
            base_interest = 8
            print("You are a Mid Tier 2. Your Base Interest Rate is", base_interest, "%")
    elif credit_score < 600:
        print("Rejected: Credit score too low.")
    else:
        print("Invalid")
else: 
    print("Rejected: Fails Baseline Criteria")
    





