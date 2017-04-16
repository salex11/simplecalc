# retrieves information to be used in equation from user
VAR1 = float(input("Please input an integer: "))
FUNC = str(input("Please input a function [add|subtract|multiply|divide]: "))
VAR2 = float(input("Please input a second integer: "))

# executes the equation
if FUNC == "add":
    print(str(VAR1 + VAR2))
elif FUNC == "subtract":
    print(str(VAR1 - VAR2))
elif FUNC == "multiply":
    print(str(VAR1 * VAR2))
elif FUNC == "divide":
    print(str(VAR1 / VAR2))
else:
    print("Please choose from one of the given functions.")
