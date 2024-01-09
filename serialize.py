import json
from collections import OrderedDict


def age_months(age):
    return int(age) * 12


with open('data.json', 'r') as f:
    person_info = json.load(f, parse_int=age_months)
print(person_info)
# print(person_info['name'])

# validate json
student = '''{
    "id": 1,
    "name": "Jessa Dug-gar",
    "class": 9,
    "attendance": 75
}'''


def validate(data):
    try:
        json.loads(data)
    except Exception as e:
        print(e)
        return False
    return True

isValid=validate(student)
if isValid:
    print('valid json')
else:
    print('invalid')