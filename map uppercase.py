#Write a program for upper case by using map function?
def name(x):
    return x.upper()
my_name = 'hi hello this is python'
updated_list = map(name,my_name)
print(updated_list)
# print(list(updated_list))
for i in updated_list:
    print(i, end="")