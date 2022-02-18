 #Write a program to clear the empty list and print the list in the list
def list(lst):
    for i in lst:
        if i!=[]:
            print(i)
list([1,[1,2],4,[],9,['hi'],[]])