age = int(input("Enter your Age : "))

if age <= 18:
    print("You are very young to Invest")
    exit(0)
elif age > 60:
    print("Sorry, You are not eligible for any plan....")
    exit(0)
else:
    income = int(input("Enter your Income : "))
    print("Congratulations, Here are some suggestions for you....")
    if age <= 40:
        if income >= 200000:
            ch = 1
        else:
            ch = 2
    elif age > 40:
        ch = 2

if ch == 1:
    print("Plan A: Invest in Land")
    print("Plan B: Invest in Construction")
    print("Plan C: Invest your money in share market ")
if ch == 2:
    print("Plan A: Invest in Saving and Mutual funds")
    print("Plan B: Invest in fix deposit 'Save for further expenditure'")