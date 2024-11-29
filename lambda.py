

# Using map() to square all elements in a list
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Using filter() to get even numbers from a list
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(evens)  # Output: [2, 4, 6]

# Using reduce() to sum all elements in a list
from functools import reduce
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(total)  # Output: 15

# Using map() to square all elements in a list
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Using filter() to get even numbers from a list
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(evens)  # Output: [2, 4, 6]

# Using reduce() to sum all elements in a list
from functools import reduce
total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(total)  # Output: 15

# Sorting a list of tuples by the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]   # pairs create list
pairs.sort(key=lambda pair: pair[1])                          # sort method is called on a tuples list, key
print(pairs)                                                  #( pair stands for a tuple pair[1] stands for second element in the tuple.
                                                              # so sorting is done by the second element of the tuple. try pair[0]

#The key parameter specifies a function that is used to extract a comparison key from each list element
#The key parameter expects a function that takes a single argument and returns a value to be used for sorting purposes.
# lambda pair:pair[1] a lambda function
# pair[1] is the expression that extracts the second element (the string) from each tuple.

print("="*70)
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
                 ]
sorted(student_tuples, key=lambda student:student[2])   # you can write key = lambda x:x[2]
print(student_tuples)          