# Functions where one function calls another to take the result and do further processing

def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def add_and_multiply(a, b, c):
    sum_result = add(a, b)  # Calling the add function
    product_result = multiply(sum_result, c)  # Calling the multiply function
    return product_result

result1 = add_and_multiply(11, 9, 1) 
result2 = add_and_multiply(2, 4, 6) 
result3 = add_and_multiply(5, 5, 5) 

print(result1) # Output = 20
print(result2) # Output = 36
print(result3) # Output = 50 
