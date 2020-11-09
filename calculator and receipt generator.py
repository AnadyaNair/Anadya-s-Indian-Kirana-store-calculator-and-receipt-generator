# This is a python program which keeps adding stream of numbers inputted by the user.
# The adding stops as soon as the user presses q key on the keyboard.

sum = 0
while(True):
    userInput = (input("Enter the price: \n")
    if (userInput!='q'):
    sum = sum + int(userInput)
    print(f"The total amount so far:₹{sum}")

    else : 
        print(f"Your total bill amount is ₹{sum}. Thanks for shopping with us! ")
        break