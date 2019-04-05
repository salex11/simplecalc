###########################################################################
# SimpleCalc Ver. 1.0 - Created by Skyy Alexander                         #
###########################################################################
# A console application that can be used to perform basic arithmetic      #
# On GitHub as salex11 @ https://github.com/salex11                       #
###########################################################################

# Asks user for two values and the mathematical operation they want to use
def valueQuery():
    value1 = float(input("What is the first value you want to do math with?: "))
    operation = str(input("What is the operation you'd like to perform? (+, -, *, /): "))
    value2 = float(input("What is the second value you want to do math with?: "))
    return value1, operation, value2;

# Performs the desired operation and prints the answer
def calculate():
    value1, operation, value2 = valueQuery()
    if operation == "+":
        answer = value1 + value2
    elif operation == "-":
        answer = value1 - value2
    elif operation == "*":
        answer = value1 * value2
    elif operation == "/":
        answer = value1 / value2
    else:
        answer = "ERROR - check to make sure your inputs were valid."
    print("The answer is: %s" % answer)
    return;

# Asks user if they would like to calculate something else
def reset():
    resetOption = input("Would you like to calculate something else? (Y/N): ")
    if resetOption == "Y":
        start = True
    elif resetOption == "N":
        start = False
        print("Thanks for using SimpleCalc!")
    else:
        start = False
        print("Invalid response... quitting SimpleCalc.")
    return start;

# Runs the calculator until the user quits
start = True
print("Welcome to SimpleCalc!")
while start == True:
    calculate()
    start = reset()

######################### THINGS TO ADD/MODIFY #########################
# 1. Spacing between text and calculations
# 2. Removal of decimal place (1.0) w/ whole numbers
# 3. Pressing a key to prompt reset()
# (i.e. "Press ENTER to calculate again or 'Q' to quit.")
# 4. Allow for lowercase "y" and "n" within reset()
