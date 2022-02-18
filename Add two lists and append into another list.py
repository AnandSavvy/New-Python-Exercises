my_lis = []
def lis(l1,l2):
    l = l1+l2
    for i in range(0,len(l1)):
        my_lis.append(l1[i]+l2[i])
        l.append(my_lis)
    print("my_lis :",my_lis)
lis([1,2,3],[4,5,6])