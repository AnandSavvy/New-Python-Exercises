#To get the sqaure of ecah number in the list by using map( function?
def s(n):
    return n**n
my_list = [1,2,3,4,5,5]
updated_list = map(s,my_list)
print(updated_list)
print(list(updated_list))