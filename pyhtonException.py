"""
Error Handling:
We may not be able to handle all errors

try :
    run code
except TypeError error
"""
a = 4
b = "7"

# print(a + b) # error

try :
    print(a + b)
except :
    print("Error: Both inputs should be numbers")

def dividenumber(a, b) :
    try : 
        result = a / b
    except ZeroDivisionError :
        print("Error: Division by zero is not allowed")
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    finally :
        return result 
try :   
    dividenumber(a, "s", "u")
except TypeError as e:
    print(f"TypeError: {e}")

stock_price = [23, 34, 54, 65]
percentage_increase = []

# Throwing an error
class insuffientPrice(Exception):
    pass

try :
    if len(stock_price) <2 :
        raise insuffientPrice("stock price must not be less than 2 days")
    for i in len(stock_price) <= 2 :
       percentage_increase.append((i - stock_price[i]) / stock_price[i-1] * 100)
except :
    insuffientPrice("error calculating percentage")

def cost(a, b):
    return a * b
print(cost(a, b))