# Examples of pathlib objects
# https://docs.python.org/3/library/pathlib.html
from pathlib import Path

input_dir = Path('./input/')
output_dir = Path('./output/')

# find all specific files in dir
data_files = list(input_dir.glob('*.dat'))
print(data_files)

# can easily be used when opening files
for file in data_files:
    # old way
    with open(input_file, 'r') as f:
        print(f.readline())

    # new way
    with file.open('r') as f:
        print(f.readline())


# easier for name handling, no need for complex string operations
dir = Path('./bla')
file = Path('file.ext')

full_file = dir / file

full_file.parent
full_file.name
full_file.suffix
full_file.with_name('setup.py')

Path.cwd()
Path.home()
full_file.exists()

# and much more (see docs)
