#Write a code by using intersection method to return new set
def a(set1,set2):
    return set1,set2
set1 = {'apple','chandu','code'}
set2 = ['ani','shal','apple','code']
set1.intersection_update(set2)
print(set1)