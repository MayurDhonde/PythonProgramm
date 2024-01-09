# # square parellel bar in pattern
#
# n=5
# for i in range(1,n+1):
#
#     for j in range(1,n+1):
#         if j==1 or j==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#
# # square plus pattern
#
# n=5
#
# for i in range(n):
#     for j in range(n):
#         if j==2 or i==2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#
# # cross pattern
# n=5
#
# for i in range(n):
#     for j in range(n):
#         if i==j or j==n-(i+1) :
#             print('*',end=" ")
#         else:
#             print(' ',end=' ')
#     print()
#
# # hollow square pattern
# n=5
#
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# 
# # hollow decreasing pattern
#
# n=6
#
# for i in range(0,n):
#     for j in range(n,i,-1):
#         if i==0 or j==n or j==i+1:
#             print('*',end=' ')
#         else:
#              print(' ',end=' ')
#
#     print()
#
# # hollow hill pattern
#
# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for k in range(0,i+1):
#         if k==0 or i==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     for m in range(0,i):
#         if m==i-1 or i==n-1:
#             print('*',end=' ')
#         else:
#             print(' ', end=' ')
#
#     print()
#
# # hollow diamond pattern
#
# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for k in range(0,i+1):
#         if k==0 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     for m in range(0,i):
#         if m==i-1 :
#             print('*',end=' ')
#         else:
#             print(' ', end=' ')
#
#     print()
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(' ',end=' ')
#     for k in range(i,n):
#         if k==i :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     for m in range(i,n):
#         if m==n-2 :
#             print('*',end=' ')
#         else:
#             print(' ', end=' ')
#     print()

name='abcdef'

