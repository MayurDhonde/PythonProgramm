import requests
import json

r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
data = r.json()

print(data)

print('-------------------------------')
#
# def clean_data(data):
#   if (isinstance(data, dict)):
#     delete = []
#     for j in data:
#       if (isinstance(data[j], dict)):
#         #print(data[j])
#         new_val = clean_data(data[j])
#         #print('newval', new_val)
#         data[j] = new_val
#
#       if (isinstance(data[j], list)):
#         new_val = clean_data(data[j])
#         data[j] = new_val
#
#       elif (isinstance(data[j], str)):
#         if (data[j] == 'N/A' or data[j] == '-' or data[j] == ''):
#           delete.append(j)
#
#
#     for i in delete:
#       del data[i]
#     return data
# print('after clean',clean_data(data))
li = []
for k, v in data.items():
    if isinstance(v, dict):
        # for key, val in v.items():
        #     if val != '' or val != '-' or val != 'N/A':

        new_dict=[key for key,value in v.items() if  value == '' or value == '-' or value == 'N/A']
        for i in new_dict:
            del v[i]
    if isinstance(v, list):
        for i in v:
            if i == ' ' or i == '-' or i == 'N/A':
                v.remove(i)
    if type(v) == 'str' or 'int':
        if v == ' ' or v == '-' or v == 'N/A':
            li.append(k)


# print(li)
for i in li:
    del data[i]

print(data)

# for k, v in data.items():
#     if isinstance(v, dict):
#         print('dictt',v)
#         for key, val in v.items():
#
#                 if val == '' or val == '-' or val == 'N/A':
#                     print(key)