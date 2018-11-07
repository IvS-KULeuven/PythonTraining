import csv
from pathlib import Path
# https://docs.python.org/3/library/csv.html


def write_csv(output_file, columns, header, delimiter=' '):
    "write csv file from iterator of tuples"

    with output_file.open('w') as out:
        out_writer = csv.writer(out, delimiter=delimiter)
        out_writer.writerow(header)
        out_writer.writerows(columns)

    print('Wrote out {}'.format(output_file.name))


def read_csv(input_file):
    with input_file.open('r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        # next(reader)  # skip header
        for line in reader:
            print(line)
        # add extra stuff


list1 = list(range(0, 300, 10))
list2 = list(range(0, 2000, 100))
out_columns = zip(list1, list2)
out_header = ['temperature (K)', 'Gibbs free energy (kJ/mol)']
out_file = Path('./output/one.csv')

write_csv(out_file, out_columns, out_header)

input_file = Path('./input/one.csv')
read_csv(input_file)

# NOTE: can also be used for reading/writing dictionaries
