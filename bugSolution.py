def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1/x 
        elif x < 0:
            return x**0.5 
        else:
            return x**2
    except TypeError:
        print("Error: Input must be a number.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

# Example demonstrating input validation and error handling
result1 = function_with_uncommon_error(5)
print(result1)  # Output: 25

result2 = function_with_uncommon_error(-4)
print(result2) # Output: Error: Input must be a number (if it's a complex, the type error will be caught) 

result3 = function_with_uncommon_error('abc')
print(result3)  # Output: Error: Input must be a number.

result4 = function_with_uncommon_error(0)
print(result4) # Output: Error: Cannot divide by zero.