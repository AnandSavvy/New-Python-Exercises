#Write a code to get the count of the positive numbers.
# to get the ocunt of the positive numbers and nembers 
list = [1,2,3,-2,-4,5,3,-4,-6,-2,-4,3,5,76,-4,-5,8,3]
pos_count = 0
neg_count = 0
for i in list:
    if i<0:
        pos_count += 1
    else:
        neg_count += 1
print('positive valuse:', pos_count )
print('negative values:', neg_count )