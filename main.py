from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def menu():
    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def main():
    while True:
        choice = menu()
        if choice == '5':
            print("Exiting Calculator. Goodbye!")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
