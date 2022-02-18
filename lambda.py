#Writing a program using lambda
def my_value(n):
    return lambda a :a*n
n = my_value(10)
print(n(2))