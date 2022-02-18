Write a program for lower case by using map function
def name(x):
    return x.lower()
my_name = 'HI HELLO PYTHON'
updated_list = map(name,my_name)
print(updated_list)
print(list(updated_list))
​