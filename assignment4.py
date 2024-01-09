# check for prime number
"""

num=int(input('enter a number'))
count=0
for i in range(2,num+1):
    if  num%i==0 :
        count+=1

if count==1:
    print('prime number')
else:
    print('not prime number')

#write next prime  number

n=int(input('enter a number'))

for i in range(n+1,):
    for j in range(2,i):
        if i%j==0:
            break
    else:

        print('prime number',i)
        break


# write n prime numbers
num=int(input('enter num'))
count=0
for i in range(2, num*num):
    for j in range(2, i ):
        if i % j == 0:
            break
    else:
        print(i)
        count+=1
        if count==num:
            break


# print all prime number between two number

a = 10
b = 20

for i in range(a, b):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


# print n odd natural number in reverse order

num = int(input('enter a number'))

count=0

for i in range(1, num*num):
    if i % 2 != 0:
        print(i)
        count+=1
        if count==num:
            break

# print n natural number in reverse order
num=int(input('enter number'))
for i in range(num*2,0,-2):
    print(i)
"""
# find lcm of two numbers


a = 2  # 3,6,9,12,15,18
b = 120 # 5,10,15,20,25
n=1
while n <= a*b:
    if n % a == 0 and n % b == 0:
        print(n)
        break
    n += 1
"""
num=1
while num<=1:
    list1=[]
    for i in range(1,10):

        list1.append(a*i)
    print(list1)
    list2=[]
    for j in range(1,10):
        list2.append(b*j)
    print(list2)
    list3=[]
    for k in list1:
        if k in list2:
            list3.append(k)
    print('LCM number is',list3[0])

    num+=1
    
"""
n = int(input())
if 1<=n<=150:
    for i in range(1,n+1):
        print(str(i),end='')