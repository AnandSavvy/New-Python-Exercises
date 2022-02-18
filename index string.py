# Write a program to find the string index in a given list
def values(lst):
    for i in lst:
        if (type(i)is str):
            print(lst.index(i))
values(['sam',65,'gsg',54,'gst'])
    