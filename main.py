def main():
    print("Welcome to the Team Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        import addition
        addition.add()
    elif choice == '2':
        import subtraction
        subtraction.subtract()
    elif choice == '3':
        import multiplication
        multiplication.multiply()
    elif choice == '4':
        import division
        division.divide()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
