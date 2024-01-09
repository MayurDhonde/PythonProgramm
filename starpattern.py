"""1
3 2
6 5 4
10 9 8 7

"""




n=7
for i in  range(1,n):
    for j in range(n,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print('*',end='')
    print()
n=8

for i in range(1,n):
    for j in range(n,i,-1):
        print(' ',end='')
    for k in range(1,i+1):
        print('*', end=' ')
    for m in range(1,i):
        print('*',end=" ")
    print()


for i in range(n):
    for j in range(0,i):
        print(' ',end='')
    for k in range(n,i,-1):
        print('*', end='')
    for m in range(n-1,i,-2):
        print('*',end="")
    for p in range(0,i-1):
        print(' ',end='')
    print()

#myself
n=6
m = 0
stop = 0

pre_start = 0
for i in range(1, n + 1):
    start = pre_start + i #3,0

    for j in range(start, stop, -1):
        print(j, end=' ')
    print()
    stop = start# 3,4
    pre_start = start #2,6


n=5
k=0
for i in range(1,n+1):

    for j in range(n,k,-1):
        print(n,end=' ')
    print()
    k+=1


n=5
for i in range(1,n+1):
    for j in range(0,n+1):
        print(j,end=' ')
    n-=1
    print()

n=9
a=1
for i in range(1,n+1):
    for j in range(0,i):
        print(a,end=" ")
    a+=2
    print()


n=5

for i in range(0,n):
    for j in range(n,0,-1):
        print(n,end=' ')
    n-=1
    print()

n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

n=9
for i in range(1,n+1):
    for j in range(i,n):
        print(' ',end=" ")
    for k in range(1,i+1):
        print(k, end=" ")
    print()

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")


n=6
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end=' ')
    print()
print()
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print('*', end=' ')
    print()


n=5
for i in range(1,n+1):
    for k in range(1,i+1):
        print(i,end=" ")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print()


n=8

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()



n=8
for i in range(1, n+1):
    for j in range(n,i,-1):
        print('*',end=" ")
    for m in range(1,i):
        print('_',end=" ")
    for p in range(1, i ):
        print('_', end=" ")
    for k in range(n,i,-1):

        print('*',end=" ")
    print()
