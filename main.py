from calculator import Calculator
from history import History
from calculation import Calculation

def main():
    calc = Calculator()
    history = History()

    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if operation == 'exit':
            break
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if operation == '+':
                result = calc.add(a, b)
            elif operation == '-':
                result = calc.subtract(a, b)
            elif operation == '*':
                result = calc.multiply(a, b)
            elif operation == '/':
                result = calc.divide(a, b)
            else:
                print("Invalid operation.")
                continue

            # Create a Calculation instance and add to history
            calculation = Calculation(f"{a} {operation} {b}", result)
            history.add_calculation(calculation)

            print(f"Result: {result}")
            print("History:")
            history.display_history()

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
