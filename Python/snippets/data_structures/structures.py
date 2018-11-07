# Examples of data structures


# --- Lists ---
# Lists Can Contain Arbitrary Objects
# Lists Are Ordered
# List Elements Can Be Accessed by Index
# Lists Can Be Nested
# Lists Are Mutable
# Lists are pointers to memory


# Lists Can Contain Arbitrary Objects
a = [21.42, 'foobar', 3, 4, 'bark', True, 3.14159]

# even complex stuff
# functions


def foo():
    pass


# classes
int
print(int)

# modules
import numpy

b = [foo, int, numpy]

# or nothing
c = []

# does not have to be unique
d = [1, 1, 'x', 'x']

# Lists Are Ordered
# List Elements Can Be Accessed by Index

a[0], a[3], a[-3], a[2:5], a[1:5:2], a[:3], a[2:]

# Lists Can Be Nested

e = [a, 'apple', ['orange', 1.1, 43], 7]

e[0], e[2][2:5], len(e), len(e[0])

# Lists Are Mutable
a
a[1] = 400
del a[1]
a[0:2] = ['fooooo', 'baaaaar']
a.append(['pear', 'banana'])
a.extend(['pear', 'banana'])
# and many other functions to manipulate lists!

# Lists are pointers to memory
a = [1, 2, 3]
b = a
b[0] = 4
print(b)
print(a)
c = a[:]
c[0] = 5
print(c)
print(a)
d = a.copy()
f = e.copy()
f[0][0] = 1
e
d[0] = 6
print(d)
print(a)

# --- Tuples ---
# Tuples are like lists except:
#   Tuples are defined by () instead of []
#   Tuples are immutable.

# https://realpython.com/python-lists-tuples/#python-tuples
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
t[0] = 'stuff'

t2 = 'x', 'r', 6
t3 = (3)
t4 = (3,)
type(t3)
type(t4)
x, y, z = (t2, [2, 3], 3)
# Why use a tuple instead of a list?

# Faster! (noticeable for big lists)
# Safety! (if those values should remain the same, in case of accidents)
# Can be key in a dictionary


# --- Dictionaries ---
# Dictionaries are like lists:
#   Both are mutable.
#   Both are dynamic. They can grow and shrink as needed.
#   Both can be nested.

# Dictionaries differ from lists:
#   Primarily in how elements are accessed
#       List elements are accessed by their position in the list, via indexing.
#       Dictionary elements are accessed via keys.
#   Unordered
#   Unique keys
#   Immutable keys
#
# https://realpython.com/python-dicts/

MLB_team = {'Colorado': 'Rockies',
            'Boston': 'Red Sox',
            'Minnesota': 'Twins',
            'Milwaukee': 'Brewers',
            'Seattle': 'Mariners',
            4: 'rr',
            'kbalbla': [1, 2, 3]
            }

MLB_team = dict([('Colorado', 'Rockies'),
                 ('Boston', 'Red Sox'),
                 ('Minnesota', 'Twins'),
                 ('Milwaukee', 'Brewers'),
                 ('Seattle', 'Mariners'),
                 (4, 'rr')]
                )

# if keys are strings:
MLB_team = dict(Colorado='Rockies',
                Boston='Red Sox',
                Minnesota='Twins',
                Milwaukee='Brewers',
                Seattle='Mariners',
                )
# accessing
MLB_team['Seattle']
# adding
MLB_team['Kansas City'] = 'Royals'

# keys and values can have mixing types
foo = {42: 'aaa', 2.78: False, True: 400}

# nested dictionaries
bar = {'MLB_team': MLB_team, 'foo': foo}
print(bar['foo'][42])
bar['MLB_team']['Seattle']
# Why use dictionaries over lists?

# Faster for look-up, no need to iterate to find values
# More user friendly accessing, no more nested indexes


# --- Sets ---
# Sets are unordered.
# Set elements are unique.
# A set itself may be modified, but the elements contained in the set must be of an immutable type.

# https://realpython.com/python-sets/

# Creating
# x = set(<iter>)
x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
x = set(('foo', 'bar', 'baz', 'foo', 'qux'))
x = set('Hellooooo')
x = {'foo', 'bar', 'baz', 'foo', 'qux'}
set(x)
# Beware of empty sets!
x = set()  # set
x = {}  # dict

# Immutable objects
x = {42, 'foo', (1, 2, 3), 3.14159}
# so no lists or dicts

# Use when you need to know unique values
# Think of it as a mathematical set (union, difference, ...)
# Frozenset, is like a set, except that it is immutable.
