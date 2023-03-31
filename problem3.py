pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

total_cents = (pennies * PENNY_VALUE) + (nickels * NICKEL_VALUE) + \
              (dimes * DIME_VALUE) + (quarters * QUARTER_VALUE)


total_dollars = total_cents / PENNIES_IN_DOLLAR
print("Enter the number of pennies :",pennies)
print("Enter the number of nickels :",nickels)
print("Enter the number of dimes :",dimes)
print("Enter the number of quaters :",quarters)
if total_dollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")

else:
    print("Congratulations!")
    print("You win the game")