# Python Program to Swap Two Elements in a List
# list1 = [12, 32, 21,  11, 22]
# pos1=2
# pos2=4
#
# list1[pos1-1],list1[pos2-1]= list1[pos2-1],list1[pos1-1]
# print(list1)

# Different ways to clear a list in Python

# numbers = [1, 2, 3, 4, 5, 6]
# for i in range(len(numbers)):
#     numbers.pop()
# print(numbers)

# Using “*= 0”
#
# numbers*=0
# print(numbers)

# python reverse list

# list_num = [1, 12, 13, 32, 4, 21,0]
# # print(list_num[-1:0:-1])
# # print([i for i in list_num[-1:0:-1]])
#
# if len(list_num)>1:
#     for i in range(len(list_num)//2):
#         list_num[i],list_num[len(list_num)-i-1]=list_num[len(list_num)-i-1],list_num[i]
#
# print(list_num)

#  Cloning or Copying a list
#
# li=[1,2,3,4,5]
#
# l2=[]
# l2.extend(li)
# print(l2)

# Python | Count occurrences of an element in a list
#
# li = [12, 11, 13, 14, 11, 10, 12, 21, 21, 2, 1, 1]
# x = 12
# # print(li.count(111))
# count=0
# for i in li :
#     if i == x:
#         count += 1
# print(count)

# Find sum and average of List in Python

# li = [12, 11, 13, 14, 11, 10]
# li_len = len(li)
# sum = 0
# for i in li:
#     sum+=i
#     avg=sum/li_len
# print('sum of li is', sum , 'and average is', avg)

# Python | Sum of number digits in List

# li = [12, 1, 4, 32, 35, 111]
#
# li2=[]
#
# for i in li:
#     add = 0
#     for j in range(len(str(i))):
#         add+=int(str(i)[j])
#     li2.append(add)
# print(li2)

# Multiply all numbers in the list

# li = [1, 2, 3, 4]
# mul=1
# for i in li:
#     mul*=i
# print(mul)

# Python program to find smallest number in a list

# li=[12, 11, 4, 32, 35, 10,111]
# min=li[0]
# for i in li:
#     if min>i:
#         min=i
# print(min)

# find the second largest number in a list
#
# li = [2, 6, 11, 4, 7,3,9,22]
#
# max=li[0]
# for i in li:
#     if i>max:
#         max=i
# temp=li[0]
# for j in li:
#     if max>j:
#         if temp<j:
#             temp=j
#
# print(temp)

# print all even numbers in list

# li = [12, 1, 234, 22, 13, 0]

# print([i for i  in li if i%2 == 0])

# Python program to print all even numbers in a range
#
# start=2
# end=12
# print(','.join([str(i) for i in range(start,end) if i % 2 == 0]))

# Python program to count Even and Odd numbers in a List

# li=[12, 1, 234, 22, 13, 0,21]
# count=0
# for i in li:
#     if i%2 == 0:
#         count+=1
# else:
#     print('odd count is', len(li)-count, 'even count is',count)

# Python program to print all positive numbers in a range

# start=-12
# end=8
# if start<0:
#     start=0
# for i in range(start,end):
#     print(i,end=" ")

# Python program to print all negative numbers in a range

# start=19
# end=9
# if start>=0 :
#     start=-1
# if end>=0:
#     end=0
#
# for i in range(start,end,-1):
#     print(i,end=" ")

# removie element from list

# li=  [12, 1, 234, 22, 13, 0]
#
# ele=[12,22]
#
# for i in ele:
#     li.remove(i)
# print(li)

# remove empty tuple

# tuples = [(), ('max',2), (12,2),(), (','), (),1]
# e=()
# for i in tuples:
#     if i == e:
#         tuples.remove(i)
# print(tuples)
#
# # remove duplicate
# list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# dublicate_ele= set()
#
# for i in list1:
#     if list1.count(i)>1:
#         dublicate_ele.add(i)
#
# print(list(dublicate_ele))

# new_list=[]
#
# for i in list1:
#     if list1.count(i)>1:
#         if i not in new_list:
#             new_list.append(i)
# print(new_list)

# remove empty list
#
# test_list = [5, 6, [], 3, [], 9,[],1]
# empty_list=[]
# new_list=[]
# for i in test_list:
#     if i != empty_list:
#         new_list.append(i)
#
# print(new_list)

# create list of dict
key_list = ['name', 'id']
test_list = ['gfg',3]

new_list=[]


k=0
for m in range(len(key_list)):
    dict = {}
    for i in key_list:
        dict[i]=test_list[k]

        k+=1
    new_list.append(dict)

print(new_list)

