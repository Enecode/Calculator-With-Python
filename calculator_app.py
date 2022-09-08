def add(first_number, second_number):
    answer = first_number + second_number
    print(str(first_number) + " + " + str(second_number) + " = " + str(answer) + "\n")


def sub(first_number, second_number):
    answer = first_number - second_number
    print(str(first_number) + " - " + str(second_number) + " = " + str(answer) + "\n")


def multiplication(first_number, second_number):
    answer = first_number * second_number
    print(str(first_number) + " * " + str(second_number) + " = " + str(answer) + "\n")


def divide(first_number, second_number):
    answer = first_number / second_number
    print(str(first_number) + " / " + str(second_number) + " = " + str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")

    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        add(first_number, second_number)

    elif choice == "b" or choice == "B":
        print("Subtraction")
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        sub(first_number, second_number)

    elif choice == "c" or choice == "C":
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        multiplication(first_number, second_number)

    elif choice == "d" or choice == "C":
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        divide(first_number, second_number)
        quit()
