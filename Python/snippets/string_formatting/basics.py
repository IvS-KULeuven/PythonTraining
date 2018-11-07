# Examples of basic string formatting

# a string can be split over lines with bracket
a = ('first part '
     'second part')

# or with triple quotes BUT note the difference with new line
# and note the extra spaces when aligning
a = '''first part
        second part'''

# bad code!
a = 'first part'\
    'second part'


# string formatting
# see https://realpython.com/python-f-strings/
x = 2
y = 3
# very old style
a = 'x is %s and y is %s' %(x, y)

# not so old style (Py 2.6+)
a = 'x is {} and y is {}'.format(x, y)

# newest styles: f-string (Py 3.6+)
a = f'x is {x} and y is {y}'

# older syles make your code look messy really quickly
# f-strings make your string more readible and have more power

star = 'HD2222'
Teff = 500
logg = 3.7
radius_au = 0.8
m1 = 2
m2 = 5

def au_to_Rsun(distance):
    return distance * 214.939

s = (f'Star {star} has Teff of {Teff} K, logg of {logg}, and a radius of'
     f' {au_to_Rsun(radius_au)} au.'
     f'It is part of a binary system with total mass of {m1+m2} solar masses')
