# example of with statement to read/write files

input_file = './input/one.dat'

# bad example
f = open(input_file, 'r')
f.readline()
f.close()

# good example
with open(input_file, 'r') as f:
    print(f.readline())

# why use with?
#   Safety, so you never forget to close it
#   Safety, in case the program crahses it will be closed properly
