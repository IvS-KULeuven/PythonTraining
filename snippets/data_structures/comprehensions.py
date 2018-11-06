# Examples of comprehensions

# List comprehension
# standard
squares = []
for x in range(10):
    squares.append(x**2)

# comprehension
squares = [x**2 for x in range(10)]

# combos
muls = [i*j for i in range(1, 5) for j in range(1, 3)]

# nested
matrix = [[1, 2], [3, 4]]
z = [[i*2 for i in j] for j in matrix]

# also for dictionaries
key_list = ['a', 'b', 'c']
val_list = [1, 2, 3]
{key: val**2 for key, val in zip(key_list, val_list)}
