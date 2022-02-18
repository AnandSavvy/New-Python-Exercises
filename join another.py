#Write a program to print a string in the reverse order with joining the some other string
# to get a string in a reverse oredr with space 
def fun(lines):
    fun = '  @'.join(reversed(lines))
    return fun
print(fun('pyhton'))
