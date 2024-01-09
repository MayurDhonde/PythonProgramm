name="Hello Python"

# case fold
case_fold=name.casefold()
print('case fold:',case_fold)
print('----------------------------')
# centre
print('centre $ with 15 width: ',name.center(15,'$'))
print('----------------------------')

# capitalize
print(name.capitalize())
print('----------------------------')

# ends with
print('checking endswith "python"=>',name.endswith('python'))
print('with tuple "(hey,Python)"',name.endswith(('hey','Python'))) # you can pass tuple
print('----------------------------')

# encode
print('encoding string: ',name.encode())
print('----------------------------')

# find
print('find method')
print(name.find('Py'))

# rfind
print('rfind')
print(name.rfind('o'))
print('----------------------------')

# isalnum
print('isalnum() method')
print(name.isalnum())
print('hellopython'.isalnum())

print('----------------------------')

# isalpha
print('isalpha method')
print('hellopython:-','hellopython'.isalpha())

print('----------------------------')

# isdigit()
print('isdigit method')
print('123232:-','123321'.isdigit())
print('1.2:-','1.2'.isdigit())

print('----------------------------')

# islower
print('islower method')
print('hello:-', 'hello'.islower(), 'heLlo:-','heLlo'.islower())

print('----------------------------')

# isnumeric
print('isnumeric method')
print('125'.isnumeric())

print('----------------------------')

# isspace
print('isspace')
print('  ', '  '.isspace())

print('----------------------------')

# istitle
print('istitle')
print(name.istitle())

print('----------------------------')

# isupper
print('isupper')
print(name.isupper())
print('HELLO','HELLO'.isupper())

print('----------------------------')

# join method
# The string join() method returns a string by joining all the elements of an iterable (list, string, tuple),
# separated by the given separator
print('join method')
print('-'.join(name))
print('$ '.join(['1','2','3','4'])) # elemenets should be string

print('----------------------------')

# ljust
print('ljust')
print(name.ljust(21,'@'))

# rjust()
print('rjsut')
print(name.rjust(17,'#'))

print('----------------------------')

# lower
print('lower')
print(name.lower())
print()
# upper
print('upper')
print(name.upper())
# swapcase
print()
print('swapcase')
print(name.swapcase())

print('----------------------------')

# lstrip
print('lstrip')
print("'    hello:-'",'   hello'.lstrip('  h'))

# rstrip
print('rstrip')
print(name.rstrip(' ohn '))

# strip
print('strip')
print(name.strip('Hone'))

print('-----------------------------------')

# partition
print('partition')
print(name.partition('lo'))

print('-----------------------------------')

# replace
print('replace')
print(name.replace('Python','World'))

print('-----------------------------------')

# splits
print('splits')
print('rsplits')
print(name.split())

print('splitlines which split string on newline character')
print('hell\nd\ndf\n'.splitlines())

print('-----------------------------------')
# title
print('title')
print('hello worlD'.title())