# import pickle

# data = {'some_key': 1234567890}

# with open('my_dict.bin', 'wb') as file:
#     pickle.dump(data, file)

# data_types = pickle.dumps(data)
# print(data_types)

# with open("my_dict.bin", 'rb') as file:
#     my_dict = pickle.load(file)

# print(my_dict)
# print(pickle.loads(data_types))

import pickle
from pprint import pprint

contacts = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

filename = 'data.pkl'

def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as f:
        pickle.dump(contacts, f)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as f:
        unpacked = pickle.load(f)
    return unpacked

load =  write_contacts_to_file(filename, contacts)
unload = read_contacts_from_file(filename) 
print(load)
pprint(unload)