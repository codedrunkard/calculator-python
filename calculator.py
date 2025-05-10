import re

def is_safe_expression(expr):
    # Allow only numbers, operators, and parentheses
    return bool(re.match(r'^[\d\s+\-*/().]+$', expr))

def calculate_bodmas(expression):
    expression = expression.replace(' ', '')  # remove spaces
    if not is_safe_expression(expression):
        return "Invalid input! Only numbers and basic operators are allowed."
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

# Example usage
while True:
    user_input = input("Enter a BODMAS expression (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    print(calculate_bodmas(user_input))