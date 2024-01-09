import age as age

# student={'name':'maxd', 'age':21, 'course':'python'}
#
# add={'weight':55}
#
# student.update(add)
# student.update([('height',5)])
# student['height']=7
# student['city']='Thane'

# print(student)

# sort the dict
# myDict = {'mavi': 10, 'arnish': 9,  'sanjeev': 15, 'yash': 2, 'suraj': 32}

# l=sorted(myDict.keys())
# print(l)
# new_dict={}
# for i in l:
#     #new_dict.update([(i,myDict[i])])
#     new_dict.update({i:myDict[i]})
# print(new_dict)

# handling missing key

# myDict = {'mavi': 10, 'arnish': 9,  'sanjeev': 15, 'yash': 2, 'suraj': 32}
#
# print(myDict.get('mavie','not found'))
#
# if 'mac' in myDict:
#     print(myDict['mac'])
# else:
#     print('not found')

# sum of all items in dict

# add={'a':123, 'b':332 ,'c':123}
# sum=0
# for i in add.values():
#     sum+=i
# print(sum)

# get size of dict in bytes
myDict = {'mavi': 10, 'arnish': 9,  'sanjeev': 15, 'yash': 2, 'suraj': 32}

print(myDict.__sizeof__())
