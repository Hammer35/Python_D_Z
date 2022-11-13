import json
from random import choice


def gen_person():
    numer = ''
    name = ''
    tel = ''

    leters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while len(numer) != 10:
        numer += choice(nums)

    while len(name) != 7:
        name += choice(leters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        numer: {
            'name': name,
            'tel': tel
        }
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = []

    data.append(person_dict)

    with open('person.json', 'w') as fl:
        json.dump(data, fl, indent=2)


for i in range(5):
    write_json(gen_person())
