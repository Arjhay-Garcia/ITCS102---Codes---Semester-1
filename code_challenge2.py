# Create a Python Script that generate the following:
# 	Money to deposit: 1540
#		something something

# How? 
# 1. Find out how to detect/take the money denominations out of the original value.
#   - Definitely revolves around division
#   - Divide it by the each denomination because that returns how much a bill can fit in the orig value. 
#   - for 1000, it works but i cant make it work on the next ones.
#   - how can i extract the remaining value though? modulus pala
#   - But how can i make it so that it retains the orig value at the last print?
# 2. Once I can do that, how can I possibly list them to each of their respective denominations?
#   - 

money = int(input("Enter amount to deposit: "))
money1 = 0 + money
money = money1

a = money // 1000
money = money % 1000

b = money // 500
money = money % 500

c = money // 200
money = money % 200

d = money // 100
money = money % 100

e = money // 50
money = money % 50

f = money // 20
money = money % 20

g = money // 10
money = money % 10

h = money // 5
money = money % 5

i = money // 1
money = money % 1

print("Your current balance is", money1)
print("1000 =", a)
print(" 500 =", b)
print(" 200 =", c)
print(" 100 =", d)
print("  50 =", e)
print("  20 =", f)
print("  10 =", g)
print("   5 =", h)
print("   1 =", i)
