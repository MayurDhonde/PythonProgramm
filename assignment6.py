"""
#LIST QUESTION
n=6
x = 2
#print list of n number
list=[]
while n>0:
    for i in range(2, x):
        if x % i == 0:
            break

    else:
        list.append(x)
        n-=1
    x+=1
print(list)



#print list of square of n natural numbers

l=[]
n=6


for j in range(1,n+1):
    l.append(j*j)

print(l)
"""

#print indices of all occurance in list

# l=[int(e) for e in input('enter a number').split(',')]
# o=int(input('enter a number to find'))
#
# print(l)
# start=0
# for i in l:
#     if i == o:
#         print(l.index(i,start))
#     start+=1

# #reverse integer
# i=14532
# val=''
# for k in range(0,5):
#     a=i%10
#     val+=str(a)
#     i=i//10
# print(val)
#
# print(i//10)

#write sum of odd n even number in list

# l=[int(e) for e in input('enter list').split(',')]
# even_sum=0
# odd_sum=0
# for i in l:
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
# print(even_sum)
# print(odd_sum)

#Write a Python function to reverse a list at a specific location.

# list=[11,12,14,55,22,21,44]
# print(list)
# start=3
# stop=6
# li=[]
# for i in range(stop,start-1,-1):
#     li.append(list[i])
# for j in li:
#     list.pop(start)
#     list.insert(start,j)
#     start+=1
#
# print(list)


