person = {
    'name': 'anfal',
    'age': 17,
    'hobbies': ['reading', 'playing games', 'sleeping']
}

print(f" {person['name']} \n {person['age']}")

person['age'] = 0
person['country'] = 'Kuwait'
print(person)
print(len(person))

person['hobbies'].append('designing')

def check_hobbies(person):
    if len(person["hobbies"]) >= 3:
        print(' you are amazing')

    else: print('try harder')

check_hobbies(person)