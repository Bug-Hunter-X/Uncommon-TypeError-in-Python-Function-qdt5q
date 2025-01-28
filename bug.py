def function_with_uncommon_error(x):
    if x == 0:
        return 1/x  # ZeroDivisionError, but let's focus on something else
    elif x < 0:
        return x**0.5 # Raises TypeError if x is a complex number or other incompatible type
    else:
        return x**2

# Example of an uncommon TypeError
result = function_with_uncommon_error('abc')
print(result)