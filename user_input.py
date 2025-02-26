# Example 1: Basic string input
def basic_input():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

# Example 2: Converting to numbers
def number_input():
    # Integer input
    age = int(input("Enter your age: "))
    print(f"In 5 years, you will be {age + 5} years old.")
    
    # Float input
    height = float(input("Enter your height in meters: "))
    print(f"Your height is {height} meters.")

# Example 3: Multiple inputs
def multiple_inputs():
    # Space-separated inputs
    x, y = input("Enter two numbers separated by space: ").split()
    x, y = int(x), int(y)
    print(f"Sum: {x + y}")
    
    # Comma-separated inputs
    a, b, c = input("Enter three values separated by comma: ").split(',')
    print(f"You entered: {a}, {b}, and {c}")

# Example 4: Input with list comprehension
def list_input():
    # Taking multiple integer inputs in a list
    numbers = list(map(int, input("Enter multiple numbers separated by space: ").split()))
    print(f"Sum of numbers: {sum(numbers)}")
    print(f"Average of numbers: {sum(numbers)/len(numbers)}")

# Example 5: Input in a loop
def loop_input():
    # Keep taking input until user enters 'quit'
    while True:
        user_input = input("Enter a command (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        print(f"You entered: {user_input}")

# Example 6: Input with validation
def validated_input():
    while True:
        try:
            age = int(input("Enter your age (must be a positive number): "))
            if age <= 0:
                print("Age must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Your age is {age}")

# Main function to demonstrate all examples
def main():
    print("Python Input Examples")
    print("=====================")
    
    print("\n1. Basic Input Example:")
    basic_input()
    
    print("\n2. Number Input Example:")
    number_input()
    
    print("\n3. Multiple Inputs Example:")
    multiple_inputs()
    
    print("\n4. List Input Example:")
    list_input()
    
    print("\n5. Loop Input Example:")
    loop_input()
    
    print("\n6. Validated Input Example:")
    validated_input()

# Run the main function if script is executed directly
if __name__ == "__main__":
    main()
