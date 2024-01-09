#print n prime numbers
def prime(n):
    i=2
    p=2
    while n>0:
        while i<p:
            if p%i==0:
                break
            i+=1
        else:
            print(p)
            n-=1
        p+=1
        i=2
prime(9)

#print count in given string

str='hello  '
print(str[0])
def countString(s):
    spl=s.split()
    spl=len(spl)
    print(spl)
countString(str)

def sum(list):
    even,odd=0,0

    for i in list:
        if i%2==0:
            even+=i
        else:
            odd+=i
    print('odd sum is ',odd)
    print('even sum is ', even)
sum([1,3,5,6,4,2,12])

#print next prime number of given number

n=8
def nextPrime(n):
    n+=1
    i=2
    count=0
    while count<1:
        while i<n:
            if n%i==0:
                break
            i+=1
        else:
            print(n)
            count+=1


        n+=1

nextPrime(n)
#print first n natural number in reverse order
n=7

def reverse(n):
    if n>0:
        print(n)
        reverse(n-1)
reverse(n)

