# Bank loan interest and Interest Rate Provider
# Loadn Engine Challenge

age = int(input("Enter your age: "))
is_employed = input("Are you currently employed? ")

if is_employed == "true" or is_employed == "True" or is_employed == "yes" or is_employed == "Yes":
    is_employed = True
elif is_employed == "false" or is_employed == "False" or is_employed == "no" or is_employed == "No":
    is_employed = False
else:
    print("Invalid")
    
credit_score = int(input("What's your Credit Score? "))
annual_income = float(input("what's your annual salary? "))
has_collateral = input("Do you have any Collateral? ")

if has_collateral == "true" or has_collateral == "True" or has_collateral == "yes" or has_collateral == "Yes":
    has_collateral = True
elif has_collateral == "false" or has_collateral == "False" or has_collateral == "no" or has_collateral == "No":
    has_collateral = False
else:
    print("Invalid")

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
    elif annual_income < 40000 and has_collateral == False: #tier2
            base_interest = 9.5
            print("You are a Low Tier 2. Your Base Interest Rate is", base_interest, "%")
    elif credit_score < 750 and has_collateral == False: 
        base_interest = 8
        print("You are a Mid Tier 2. Your Base Interest Rate is", base_interest, "%")
    elif 600 <= credit_score < 750 and has_collateral == True:
            base_interest = 7
            print("You are a High Tier 2. Your Base Interest Rate is", base_interest, "%")
    elif credit_score < 600:
        print("Rejected: Credit score too low.")
    else:
        print("Invalid")
else: 
    print("Rejected: Fails Baseline Criteria")
    
