#print 10 natural number in revrese order
'''
i=10
while i>=1:
    print(i)
    i-=1

#print 10 odd natural numbers

i=1
count=0
while i<=100:
    if i%2!=0:
        print(i)
        count+=1
        if count==10:
            break
        i+=1


#sum of n natural numbers

num=int(input('enter a number'))
sum=0
while num>=1:
    sum+=num
    num-=1
print(sum)


#sum of n odd natural numbers
num=int(input('enter a number'))
sum=0
while num>=1:
    if num%2!=0:
        sum+=num
    num-=1

print(sum)

#factoroal of number

n=int(input('enter a number'))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

n=int(input('enter a number'))
prod=1
while 1<=n :
    prod=prod*n
    n-=1
print(prod)
'''
