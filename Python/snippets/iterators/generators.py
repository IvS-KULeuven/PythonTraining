# Examples of generators

# Generators are functions that can be paused and resumed on the fly,
# returning an object that can be iterated over. Unlike lists, they are lazy
# and thus produce items one at a time and only when asked.
# So they are much more memory efficient when dealing with large datasets.

# Basically: replace 'return' with 'yield' in your functions
nums = list(range(20))


def get_items(lst):
    for i in lst:
        print(i)


def gen_get_items(iter_source):
    for i in iter_source:
        yield i


get_items(nums)
# like this, it is just a generator object, it does not do anything
gen_get_items(nums)
# you need to iterate over the object, e.g.
list(gen_get_items(nums))


# example to extract limited amount of info from large file
def parse_large_data_file(source_iter):
    # search keys for input file
    rot_symmetry_key = 'Rotational symmetry number'
    vib_frequencies_key = 'Frequencies --'
    rot_temperatures_key = 'Rotational temperature'

    rot_symmetry = []
    vib_frequencies = []
    rot_temperatures = []

    for row in source_iter:
        if rot_symmetry_key in row:
            rot_symmetry = clean_input_string(row, rot_symmetry_key)

        elif vib_frequencies_key in row:
            cleaned_row = clean_input_string(row, vib_frequencies_key)
            for i in cleaned_row:
                vib_frequencies.append(i)

        elif rot_temperatures_key in row:
            rot_temperatures = clean_input_string(
                                    row, rot_temperatures_key)

    yield rot_symmetry
    yield vib_frequencies
    yield rot_temperatures


data = list(parse_large_data_file(f))
rot_symmetry, vib_frequencies, rot_temperatures = data


# example
