# function that runs a generic plot (e.g. using matplotlib)
def plot_function(x, y):
    # do some plotting of x vs y
    pass


# function to find an index of a matching value in another dataset
def find_matching_id(input_data, star_to_match):
    # define a function to match the data,
    # there are a few different ways to do this
    pass


# ---practical structure examples---

# 1) use multiple lists for different catagories/values
#    + lists are simple to create and understand
#    - can end up with many lists/namespaces to keep track of
#    - make sure lists are same length, tricky if data is missing
star_names_1 = ['HD11111', 'HD22222', 'Sun']
Teff_1 = [1111, 2222, 5778]
spectra_wav_1 = [[4201., 4201.1, 4201.2, 4201.3], [4204., 4223.5, 5677.6],
                 [4201., 4201.1, 4201.2, 4201.3]]
spectra_flux_1 = [[0.9, 0.1, 0.2, 0.3], [34343, 9556, 77865],
                  [0.9, 0.1, 0.2, 0.3]]

# 2) use nested lists to group parameters
#    - trickier to initially group the data and understand structure
#    + namespace is tidier
#    - still need to use indexes
stardata_2 = [['HD11111', 1111, [4201., 4201.1, 4201.2], [0.9, 0.1, 0.2]],
              ['HD22222', 2222, [4204., 4223.5, 5677.6], [34343, 9556, 77865]],
              ['Sun', 5778, [4201., 4201.1, 4201.2], [0.9, 0.1, 0.2]]]
stardata_2[2][1]
# 3) use nested dictionaries to group parameters!
#    - trickier/longer to initialise compared to non-nested lists
#    + namespace is very clean
#    + can use human-readable keywords instead of indexes
#    + Keywords can negate the need for iterative searching
stardata_3 = {'HD11111': {'Teff': 1111, 'wav': [4201., 4201.1, 4201.2],
                          'flux': [0.9, 0.1, 0.2]},
              'HD22222': {'Teff': 2222, 'wav': [4204., 4223.5, 5677.6],
                          'flux': [34343, 9556, 77865], 'badfluxes': True},
              'Sun': {'Teff': 5778, 'wav': [4201., 4201.1, 4201.2],
                      'flux': [0.9, 0.1, 0.2]}
              }

stardata_3['Sun']['Teff']
# ---a) how to simply iterate over the data structures---

# 1) multiple lists
#    iterate over range with len == len(array)
for i in range(len(star_names_1)):
    print('Star: ', star_names_1[i], ' Teff:', Teff_1[i])
    plot_function(spectra_wav_1[i], spectra_flux_1[i])

#    use enumerate() function, like above but first list items
#    are retained as a variable
for idx, name in enumerate(star_names_1):
    print('Star: ', name, ' Teff:', Teff_1[idx])
    plot_function(spectra_wav_1[idx], spectra_flux_1[idx])

# 2) list of lists
#    this time we iterate over the list items, with each item being a list
for star in stardata_2:
    print('Star: ', star[0], ' Teff:', star[1])
    plot_function(star[2], star[3])

#    again, enumerate() can be used to work with both the idx and the item
for idx, star in enumerate(stardata_2):
    print('Star: ', star[0], ' Teff:', star[1])
    plot_function(star[2], star[3])

# 3) dictionary of dictionaries
#    the dict.items() returns a list of (key, value) tuple pairs
#    in this example the value is a dictionary itself, with its own keywords
for key, val in stardata_3.items():
    print('Star: ', key, ' Teff:', val['Teff'])
    plot_function(val['wav'], val['flux'])


# ---b) how to iterate over a subset of stars/objects---

# define your subset
subset = ['HD1111', 'Sun']

# option I) iterate over all data, use if statement to check for membership
#           - a lot of needless iterations if structure is large
for idx, name in enumerate(star_names_1):
    if name in subset:
        print('Star: ', name, ' Teff:', Teff_1[idx])


# option II) iterate over the subset, use if statement to check for membership
#            when using 1) multiple lists, or 2) list of lists then need to
#            find the matching indexes prior to work

for idx, name in enumerate(subset):
    if name in star_names_1:
        matched_id = find_matching_id(star_names_1, name)  # return matched idx
        print('Star: ', name, ' Teff:', Teff_1[matched_id])

#            or 3) dictionary of dictionaries - if subset values are keywords
#            in dict of data then problem becomes trivial
for name in subset:
    print name, stardata_3[name]['Teff']

# there are many other ways to work with data structures, including several
# faster ways that are more advanced than these examples
