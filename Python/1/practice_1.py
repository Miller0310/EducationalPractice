from itertools import permutations
from Validator import Validator

validator = Validator()

try:
    N = validator.integer(input("Enter N: "))
    K = validator.integer(input("Enter K: "))
except Exception as e:
    print(e)
    exit(1)

string = ''
for i in range(1, N + 1, 1):
    string += str(i)

outer_counter = 0
for i in permutations(string):
    index = 1
    inner_counter = 0
    for j in i:
        if int(j) == index:
            inner_counter += 1
        index += 1
    if inner_counter == K:
        outer_counter += 1

print(outer_counter)
