# reverse the string
# name='python love I'
# a=[]
#
# for i in name.split().__reversed__():
#     a.append(i)
# print(' '.join(a))
import random
import string
# check whether the string is Symmetrical or Palindrome

# n = 'abcba'
# l = len(n)
# if l % 2 == 0:
#     div = l/2
#     if n[0:int(div)] == n[int(div):]:
#
#         print('string is symmetrical')
#     else:
#         print('not')
#
# n='abcba'
# r=[i for i in n].__reversed__()
#
# if n == ''.join([j for j in r]):
#     print('string is palindrome')
# else:
#     print('nnn')

# n='hello world'
# str=""
# for i in range(len(n)):
#     if i == 0 or i==len(n)-1:
#         str+=n[i].upper()
#     else:
#         str+=n[i]
# print(str)

# check given string has atleast one string or character
#
# n='as12'
# a=0
# b=0
# for i in n:
#     if i.isalpha() :
#        a+=1
#     if i.isnumeric():
#         b+=1
#
# if a and b >0:
#     print('True')
# else:
#     print('False')

# accept the string that contains all owel

# vowels =['a','e','i','o','u']
# v2=['A','E','I','O','U']
# s='THIS IS BEST THOUGHT AA '
# count=0
# c=0
# for i in s:
#     if i in vowels:
#         count+=1
#     if i in v2:
#         c+=1
# print(count,c)
# if count>=5 or c >=5:
#     print('accepted')
# else:
#     print('not accepted')

# Count the Number of matching characters in a pair of string

# a='abnco'
# b='asamsb'
#
# s1=set(a)
# s2=set(b)
#
# print(len(s1.intersection(s2)))

# Python program to count number of vowels using sets in given string

# n='GeeksforGeeks'
# vowels=['a','e','i','o','u']
# add=0
# for i in vowels:
#     # if i in n.lower():
#     add+=n.lower().count(i)
#
# print(add)

# Remove all duplicates from a given string in Python

# n='geeksforgeeks'
# new_str=''
# for i in n:
#     if i not in new_str:
#         new_str+=i
#
# print(new_str)

# Python – Odd Frequency Characters

# n='geekforgeeks'
# li=[]
# for i in n:
#     if n.count(i)%2 != 0:
#         li.append(i)
# print(li)

# Python – Specific Characters Frequency in String List
# test_list = ['geeksforgeeks is best for geeks']
# chr_list=['e','s']
# dict={}
# print( { i : str(test_list[0].count(i)) for i in chr_list if i in str(test_list[0])})
# # print(str(test_list[0].count('e')))
# for i in chr_list:
#     if i in str(test_list[0]):
#         dict[i]=str(test_list[0].count(i))
# print(dict)

# Python | Frequency of numbers in String

# n='geeks 4 geeks is no 11'
# count=0
# for i in n:
#     if i.isnumeric():
#         count+=1
# print(count)

# Program to check if a string contains any special character

# n = 'hello @world'
# print(n.isalpha())

# Generating random strings until a given string is generated

# n='gfg'
# flag=True
# l = 0
# while flag:
#     for i in random.choice(string.ascii_letters):
#         if i == n[l]:
#             print(i)
#             l += 1
#             if l == len(n):
#                 flag=False
#

# Find words which are greater than given length k

# k=4
# n='hello how r u doing'
# li=[]
# for i in n.split():
#     if len(i)>=k:
#         li.append(i)
# print(li)

# Python program for removing i-th character from a string

# n='geeks for geek'
# i=7
#
# print(n[:i-1]+n[i:])

# find uncommon words in string

# A = 'Geeks for Geeks'
# B = 'Learning from Geeks for Geeks'
# li=[]
# if len(A)<len(B):
#     A,B=B,A
# for i in A.split():
#     if i in B.split():
#         pass
#     else:
#         li.append(i)
# print(li)
#
#
# n='14,625,498.002'
#
# new_str=''
# for i in n:
#     new_str += i
#     if i == ',':
#         new_str=new_str.replace(',','t')
#     if i == '.':
#         new_str=new_str.replace('.',',')
#
#
# print(new_str.replace('t','.'))