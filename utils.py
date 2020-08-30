import json


def get_known_dogs(filename):
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            return data['dogs']
    except (OSError, IOError) as e:
        return []


def save_new_dogs(filename, known_dogs, new_dogs):
    dogs = known_dogs
    for dog in new_dogs:
        dogs.append(dog)
    with open(filename, 'w') as json_file:
        data = {"dogs": dogs}
        json.dump(data, json_file, indent=4)


def find_new_dogs(known_dogs, current_dogs):
    new_dogs = []
    for dog in current_dogs:
        if dog not in known_dogs:
            new_dogs.append(dog)
    return new_dogs
