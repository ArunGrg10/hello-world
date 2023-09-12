print("The price of the house is $1M")
price = 1000000
good_buyer_credit = False
bad_buyer_credit = True

if good_buyer_credit:
    print('The buyer has a good credit')
    down_payment= 0.1 * price
    print(f"down payment= ${down_payment}")

elif bad_buyer_credit:
    print('the buyer has bad credit')
    down_payment= 0.2 * price
    print(f"${down_payment} is the total down payment he has to pay.")
else:
    print('The buyer cannot buy the house.')




abc = 'LOGICAL OPERATOR'
print(abc)
good_behavior= False
good_speaking= False

if good_speaking and good_behavior:
    print(" the student is eligble for admission.")
elif good_speaking or good_behavior:
    print(" The student has to give entrance exam for admission")
else:
    print("The student is nor eligible for admission")

xyz= 'Comparative operator'

x= input('the current temperture of a room is:')

if int(x) < 30:
    print("turn off the AC")
elif int(x) > 30:
    print("turn on the AC")
else:
    print("leave it as it is.")

name = 'p'
if len(name) > 20:
    print('the character of name should be less than 20.')
elif len(name) < 2:
    print('the character of name should be at least 2.')
else:
    print(name)

weight = int(input('weight: '))
unit = input('(L)bs or (k): ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are {converted} kilos ')
else: 
    converted = weight / 0.45
    print(f'You are {converted} puounds')



