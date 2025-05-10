import re
import math

def preprocess(expression):
    # Replace caret with exponent operator
    expression = expression.replace('^', '**')
    
    # Replace square symbols like 5² with 5**2
    expression = re.sub(r'(\d+)²', r'(\1**2)', expression)

    # Replace sqrt(x) with math.sqrt(x)
    expression = re.sub(r'sqrt\(([^)]+)\)', r'math.sqrt(\1)', expression)

    return expression

def is_safe_expression(expr):
    # Only allow numbers, operators, parentheses, and valid keywords
    return bool(re.match(r'^[\d\s+\-*/().^sqrt²]+$', expr))

def calculate_advanced(expression):
    expression = expression.replace(' ', '')  # Remove spaces
    if not is_safe_expression(expression):
        return "? Invalid input! Only numbers and basic operators (plus ^, sqrt, ²) are allowed."

    try:
        safe_expr = preprocess(expression)
        result = eval(safe_expr, {"__builtins__": None, "math": math})
        return f"? Result: {result}"
    except Exception as e:
        return f"?? Error: {e}"

# Example usage
while True:
    user_input = input("Enter expression (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    print(calculate_advanced(user_input))
