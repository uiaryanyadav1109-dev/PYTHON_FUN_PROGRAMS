# Program to make a fully upgraded simple calculator

import math


# ==========================================
#           CALCULATOR FUNCTIONS
# ==========================================

# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def sub(a, b):
    return a - b


# Function for multiplication
def mul(a, b):
    return a * b


# Function for division
def div(a, b):
    if b == 0:
        return None

    quotient = a // b
    remainder = a % b
    result = a / b

    return result, quotient, remainder


# Function for square root
def sqr(a):
    if a < 0:
        return None

    return math.sqrt(a)


# Function for power
def power(a, b):
    return a ** b


# Function for percentage
def percentage(a, b):
    if b == 0:
        return None

    return (a / b) * 100


# Function for factorial
def factorial(a):
    if a < 0 or a != int(a):
        return None

    return math.factorial(int(a))


# Function for absolute value
def absolute(a):
    return abs(a)


# ==========================================
#              CALCULATOR
# ==========================================

print("\n")
print("==========================================")
print("             CALCULATOR")
print("==========================================")


# List to store calculation history
history = []


# ==========================================
#             MAIN PROGRAM
# ==========================================

while True:

    print("\n------------------------------------------")
    print("       CHOOSE AN OPERATION")
    print("------------------------------------------")

    print("\n\t1. ADDITION")
    print("\t2. SUBTRACTION")
    print("\t3. MULTIPLICATION")
    print("\t4. DIVISION")
    print("\t5. SQUARE ROOT")
    print("\t6. POWER")
    print("\t7. PERCENTAGE")
    print("\t8. CALCULATION HISTORY")
    print("\t9. CLEAR HISTORY")
    print("\t10. FACTORIAL")
    print("\t11. ABSOLUTE VALUE")
    print("\t12. EXIT")

    print("\n------------------------------------------")


    # ======================================
    #       GET MENU CHOICE
    # ======================================

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("\nError: Please enter a valid number.")
        continue


    # ======================================
    #           ADDITION
    # ======================================

    if choice == 1:

        try:
            print("\nEnter the two numbers:")

            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            result = add(num1, num2)

            print("\nThe sum is : %s" % result)

            history.append(
                "%s + %s = %s" % (num1, num2, result)
            )

        except ValueError:
            print("\nError: Please enter valid numbers.")


    # ======================================
    #          SUBTRACTION
    # ======================================

    elif choice == 2:

        try:
            print("\nEnter the two numbers:")

            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            result = sub(num1, num2)

            print("\nThe difference is : %s" % result)

            history.append(
                "%s - %s = %s" % (num1, num2, result)
            )

        except ValueError:
            print("\nError: Please enter valid numbers.")


    # ======================================
    #         MULTIPLICATION
    # ======================================

    elif choice == 3:

        try:
            print("\nEnter the two numbers:")

            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            result = mul(num1, num2)

            print("\nThe product is : %s" % result)

            history.append(
                "%s × %s = %s" % (num1, num2, result)
            )

        except ValueError:
            print("\nError: Please enter valid numbers.")


    # ======================================
    #             DIVISION
    # ======================================

    elif choice == 4:

        try:
            print("\nEnter the two numbers:")

            num1 = float(input("Dividend: "))
            num2 = float(input("Divisor: "))

            result = div(num1, num2)

            if result is None:

                print("\nError: Cannot divide by zero.")

            else:

                division_result, quotient, remainder = result

                print("\nThe division is : %s" % division_result)
                print("The quotient is : %s" % quotient)
                print("The remainder is : %s" % remainder)

                history.append(
                    "%s / %s = %s"
                    % (num1, num2, division_result)
                )

        except ValueError:
            print("\nError: Please enter valid numbers.")


    # ======================================
    #           SQUARE ROOT
    # ======================================

    elif choice == 5:

        try:
            num1 = float(
                input("\nEnter the number: ")
            )

            result = sqr(num1)

            if result is None:

                print(
                    "\nError: Square root of a "
                    "negative number is not possible."
                )

            else:

                print(
                    "\nThe square root is : %s"
                    % result
                )

                history.append(
                    "√%s = %s" % (num1, result)
                )

        except ValueError:
            print("\nError: Please enter a valid number.")


    # ======================================
    #                POWER
    # ======================================

    elif choice == 6:

        try:
            print("\nEnter the numbers:")

            num1 = float(
                input("Base: ")
            )

            num2 = float(
                input("Exponent: ")
            )

            result = power(num1, num2)

            print("\nThe result is : %s" % result)

            history.append(
                "%s ^ %s = %s"
                % (num1, num2, result)
            )

        except ValueError:
            print("\nError: Please enter valid numbers.")


    # ======================================
    #              PERCENTAGE
    # ======================================

    elif choice == 7:

        try:
            num1 = float(
                input("\nEnter the obtained value: ")
            )

            num2 = float(
                input("Enter the total value: ")
            )

            result = percentage(num1, num2)

            if result is None:

                print(
                    "\nError: Total value cannot be zero."
                )

            else:

                print(
                    "\nThe percentage is : %.2f%%"
                    % result
                )

                history.append(
                    "%s / %s × 100 = %.2f%%"
                    % (num1, num2, result)
                )

        except ValueError:
            print("\nError: Please enter valid numbers.")


    # ======================================
    #         CALCULATION HISTORY
    # ======================================

    elif choice == 8:

        print("\n")
        print("==========================================")
        print("          CALCULATION HISTORY")
        print("==========================================")

        if len(history) == 0:

            print("\nNo calculations have been performed yet.")

        else:

            for i, calculation in enumerate(history, 1):

                print(
                    "%d. %s"
                    % (i, calculation)
                )


    # ======================================
    #            CLEAR HISTORY
    # ======================================

    elif choice == 9:

        if len(history) == 0:

            print("\nHistory is already empty.")

        else:

            history.clear()

            print("\nCalculation history cleared successfully.")


    # ======================================
    #              FACTORIAL
    # ======================================

    elif choice == 10:

        try:
            num1 = float(
                input("\nEnter a non-negative integer: ")
            )

            result = factorial(num1)

            if result is None:

                print(
                    "\nError: Factorial is only available "
                    "for non-negative integers."
                )

            else:

                print(
                    "\nThe factorial is : %s"
                    % result
                )

                history.append(
                    "%s! = %s"
                    % (int(num1), result)
                )

        except ValueError:
            print("\nError: Please enter a valid number.")


    # ======================================
    #           ABSOLUTE VALUE
    # ======================================

    elif choice == 11:

        try:
            num1 = float(
                input("\nEnter the number: ")
            )

            result = absolute(num1)

            print(
                "\nThe absolute value is : %s"
                % result
            )

            history.append(
                "|%s| = %s"
                % (num1, result)
            )

        except ValueError:
            print("\nError: Please enter a valid number.")


    # ======================================
    #                 EXIT
    # ======================================

    elif choice == 12:

        print("\n")
        print("==========================================")
        print("       THANK YOU FOR USING CALCULATOR")
        print("==========================================")
        print("                 Goodbye!")
        print("==========================================")

        break


    # ======================================
    #           INVALID CHOICE
    # ======================================

    else:

        print("\nError: Invalid choice!")
        print("Please select a number from 1 to 12.")


# ==========================================
#              END OF PROGRAM
# ==========================================