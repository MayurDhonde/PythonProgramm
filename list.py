list=[1,2,3,4,5,5]
#list is orderd, mutable,heterogenous and contain duplicate value
#list is access by index, loop
#can change value using index
print('index is',list.index(3))

append=list.append(21)
print('after append', list)

extend=list.extend([13,45])
print('after extend',list)

insert =list.insert(1,12)
print('after inser at position 1', list)

remove=list.remove(12)
print('after removing 12 list is', list)

print('count of 5 in list is ', list.count(5))

print('pop method removed index at 1', list.pop(1))

reverse=list.reverse()
print('after reversing list using reverse method', list)

sort=list.sort()
print('after sorting list', list)

list2=list.copy()
print('after copying list ,list2 is', list2)

list2.append('a')
print('after modifying list 2 the list2 is', list2, 'but list object is ', list)

list2.clear()
print('after using clear method list2 is', list2)

print(dir(list))