#sum of elements in tuple
# t=(1,23,4,5,21)
# sum=0
# for i in t:
#     sum+=i
# print(sum)

#create homogenous elements from hetrogenous elemenets

# x=(12,2,2.3,'1','abc')
# int=[]
# str=[]
# float=[]
# for e in x:
#     if type(e)==type(1):
#
#         int.append(e)
#     if type(e)==type('str'):
#
#         str.append(e)
#     if type(e)==type(1):
#
#         float.append(e)
# print(tuple(int),tuple(str),tuple(float))
# t1=('12',21,11)
# t2=(12,21,11,)
# for i in range(0,len(t1)):
#     if t1[i]==t2[i]:
#         pass
#     else:
#         print('no same elements')
#         break
# else:
#     print('yes its ordered')

#find the greatest numberr in tuple

# tup=(52,3,45,11,41)
# max=tup[0]
# for i in tup:
#     if max<i:
#         max=i
# print(max)

for i in range(1,4+1):
    for j in range(1,i+1):
        print(j,end='')
    print()