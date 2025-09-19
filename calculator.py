# Task 2: Simple Calculator



def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "⚠ Cannot divide by zero"

def calculator():
    print("\n--- Simple Calculator ---")
    while True:
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("👋 Exiting Calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)
                    print(f"✅ {num1} + {num2} = {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"✅ {num1} - {num2} = {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"✅ {num1} * {num2} = {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"✅ {num1} / {num2} = {result}")
            except ValueError:
                print("⚠ Invalid input! Please enter numbers only.")
        else:
            print("⚠ Invalid choice! Please select from 1-5.")

if __name__ == "__main__":
    calculator()
