age = int(input("AGE: "))
rev = float(input("MONTHLY REVENUE: "))
cs = int(input("CREDIT SCORE: "))
yrs = float(input("YEARS IN BUSINESS: "))
has_defaults = input("DEFAULTS?: ")
col_n = input("COLLATERAL NAME: ")
col_v = int(input("COLLATERAL VALUE: "))

if has_defaults == "True" or has_defaults == "true" or has_defaults == "yes" or has_defaults == "YES" or has_defaults == "Yes":
    has_defaults = True
else: 
    has_defaults = False

max_loan = 0
base_fee = 0

if age >= 21 and yrs >= 2 and has_defaults == False:
    if cs >= 720: # tier 1
        max_loan = rev * 3
        if rev >= 50000:
            base_fee = max_loan * 0.015
            print("Base Fee: ", base_fee)
        else: 
            base_fee = max_loan * 0.025
            print("Base Fee: ", base_fee)
            
        if col_v >= max_loan:
            print("Accepted")
        else:
            print("REJECTED: Insufficient Collateral Value")
            
        if col_v % 5000 != 0:
            base_fee += 250
        else:
            base_fee = base_fee
            
    elif cs <= 620 and cs < 720: #tier 2
        max_loan = rev * 1.5
        if yrs >= 5:
            base_fee = max_loan * 0.02
            print("Base Fee: ", base_fee)
        else: 
            base_fee = max_loan * 0.035
            print("Base Fee: ", base_fee)
            
        if col_v >= max_loan:
            print("Accepted")
        else:
            print("REJECTED: Insufficient Collateral Value")
            
        if col_v % 5000 != 0:
            base_fee += 250
        else:
            base_fee = base_fee
            
        
    elif cs < 620: #tier 3
        print("Credit Score Too Low")
    else: 
        print("INVALID")
        
    print("\n\n\nRECEIPT:")
    print("AGE --->", age)
    print("MONYTHLY REVENUE --->", rev)
    print("CREDIT SCORE --->", cs)
    print("YEARS IN BUSINESS --->", yrs)
    print("DEFAULTS? --->", has_defaults)
    print("COLLATERAL NAME? --->", col_n)
    print("COLLATERAL VALUE? --->", col_v)
    print("\n\n\n")
    print("MAXIMUM LOAN: ", max_loan)
    print("BASE PROCESSING FEE: ", base_fee)
    
else: 
    print("Failed to attain Baseline")



