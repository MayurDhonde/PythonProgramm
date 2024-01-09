# s = {1, 2, 3, 4, 5,11}
# s2={12,1,2,7,8,9,0}
#
# for i in range(len(s2)):
#     s2.pop()
# print(s2)

# Check if two lists have at-least one element common

# l1 = [1, 2, 4, 5, 6]
# l2 = [2, 3, 5, 6]
#
# for i in l1:
#     if i in l2:
#         print(True)
#         break

# find common element

# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# s1=set(ar1)
# s2=set(ar2)
# s3=set(ar3)
#
# common=s1.intersection(s2)
# result=common.intersection(s3)
# print(result)

# find missing and addition value in set
#
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [4,5, 6, 7, 8]
#
# s1=set(l1)
# s2=set(l2)
#
# diff=s1.difference(s2)
# diff2=s2.difference(s1)
#
# print('addition value', list(diff),'missing value', list(diff2))
#
# print('addition value', list(diff2),'missing value', list(diff))

# find differnce

# list1 = [10, 15, 20, 25, 30, 35, 40]
# list2 = [25, 40, 35]
#
# s1=set(list1)
# s2=set(list2)
#
# print(s1.symmetric_difference(s2))

# concat string remove uncommon

# S1 = 'aacdb'
# S2 = 'gafd'
#
#
#

# check string is paragram
#
# alphabets="abcdefghijklmnopqrstuvwxyz"
#
# str="The quick brown fox jumps over the lazy dog"
#
# for i in str.replace(' ','').lower():
#     if i in alphabets:
#         pass
#     else:
#         print(i)
#         print('not paragram')
#         break
# else:
#     print('paragram')

# Check whether a given string is Heterogram or not

# S = "the big dwarf only jumps "
#
# for i in S.replace(' ',''):
#     if S.count(i)>1:
#         print('not')
#         break
# else:
#     print('heterogram')


