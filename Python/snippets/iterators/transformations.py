# Examples od using map() and filter()


# filter(function, iterable) is equivalent to the generator expression
# (item for item in iterable if function(item)).
def skip_even_nums(num):
    return num % 2 != 0


# same but explicitly written the generator
def skip_even_nums_gen(nums):
    for num in nums:
        if num % 2 != 0:
            yield num


nums = list(range(20))
# this returns a generator, so needs be be iterator over
odds_gen = filter(skip_even_nums, nums)
odds = list(odds_gen)

# use explicit generator
list(skip_even_nums_gen(nums))


# map() function - applying transformations to a collection
def square_nums(num):
    return num**2


squared_gen = map(square_nums, nums)
squared = list(squared_gen)
