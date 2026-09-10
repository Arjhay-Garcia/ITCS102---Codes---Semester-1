# Global Freight Calculator

# ======================================================= #
# USER INPUTS
# ======================================================= #
sender = str(input("Sender Name: "))


item = str(input("Item: "))


is_fragile = (input("Fragile? "))

if is_fragile == "True" or is_fragile == "Yes" or is_fragile == "yes":
	is_fragile = True
else:
	is_fragile = False


weight = float(input("Weight of the Item: "))


distance = float(input("Distance: "))


is_express = (input("Express: "))

if is_express == "True" or is_express == "Yes" or is_express == "yes":
	is_express = True
else:
	is_express = False



is_international = input("International? ")

if is_international == "True" or is_international == "Yes" or is_international == "yes":
	is_international = True
else:
	is_international = False



# ======================================================= #
# CALCULATION / FORMULA
# ======================================================= #

base_cost = (weight * 2.50) + (distance * 0.15)


if is_international == True and is_express == True:
	total = (base_cost * 1.40) + 50
else: 
	if is_express == True or is_international == True and weight > 20:
		total = (base_cost * 1.20) + 25
	else: 
		if weight > 30 or distance > 1000:
			total = base_cost + 30
		else:
			if weight <= 2 and distance <= 100 and is_international == False and is_express == False:
        			total = 0
			else:
				total = base_cost

# ======================================================= #
# BOOLEAN TO STRING
# ======================================================= #
if is_fragile == True:
	is_fragile = "Yes"
else:
	is_fragile = "No"
    
    
if is_express == True:
	is_express = "Yes"
else:
	is_express = "No"
    

if is_international == True:
	is_international = "Yes"
else:
	is_international = "No"


# ======================================================= #
# RESULTS / OUTPUT
# ======================================================= #

print("\n\nSHIPPING DETAILS")
print("Sender Name:\t", sender)
print("Item:\t\t", item)
print("Fragile:\t", is_fragile)
print("Weight:\t\t", weight, "kg")
print("Distance:\t", distance, "km")
print("Express:\t", is_express)
print("International:\t", is_international)

print("\nYour shipping fee is", total)
