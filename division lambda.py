 #Write a function to given a number is divisible by using lambda function ?
def s(lst):
    result = print(filter(lambda x:(x%2==0),lst))
    return(result)
s([29,20,3,4,1,5])