# example to use json module
import json
from pathlib import Path


def read_json(input):
    "returns dict of json file"
    with input.open('r') as f:
        clusters = json.load(f)

    return clusters


def write_json(out_dict, out_file):
    "write dict into json file"
    with out_file.open('w') as f:
        json.dump(out_dict, fp=f, indent=4)


# read json file into dictionary
input_file = Path('./input/one.json')
new_dict = read_json(input_file)
print(new_dict)


# write dictionary to json file
output_file = Path('./output/out.json')
stardata = {'HD11111': {'Teff': 1111, 'wav': [4201., 4201.1, 4201.2],
                        'flux': [0.9, 0.1, 0.2]},
            'HD22222': {'Teff': 2222, 'wav': None, 'flux': None,
                        'baddata': True},
            'Sun': {'Teff': 5778, 'wav': [4201., 4201.1, 4201.2],
                    'flux': [0.9, 0.1, 0.2]}
            }
write_json(stardata, output_file)
