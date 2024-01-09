# s={12,2,3,21,4}
# s2={12,3,54,2}

# for e in s.intersection(s2):
#
#     print(e)
#print n prime numbers
# s=set()
# n=2
# c=6
#
# while c>0:
#     for i in range(2,n):
#         if n%i == 0:
#             n+=1
#             break
#     else:
#         s.add(n)
#         c-=1
#         n+=1
#
# print(s)

#union of two sets
u1={12,3,4,5}
u2={2,12,3,4,6}

print(u1.union(u2))

#count elemene in set

count=0

for i in u1:
    count+=1
print(count)