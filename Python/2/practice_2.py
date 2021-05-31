import random

try:
    N = int(input("Enter N to generate array: "))
except Exception as e:
    print(e)
    exit(1)

array = [random.randint(0, N) for i in range(N)]
array.sort()
print("Array: ", array)

try:
    K = int(input("Enter K: "))
except Exception as e:
    print(e)
    exit(1)
    
size = len(array)  # 1
result = []  # 1
middle = size // 2  # 2
high = size - 1  # 2
operation_counter = 7  # 1
for i in range(size):
    if array[middle] == K:  # 1
        copy_middle = middle  # 1
        while array[middle] == K:  # 1 operation All cycle:4*m
            result.append(middle)  # 1
            middle -= 1  # 1
            operation_counter += 4  # 1
            print("array[middle] == K. Count of operation:", operation_counter)
        middle = copy_middle + 1  # 2
        while array[middle] == K:  # 1 operation All cycle:4*p
            result.append(middle)  # 1
            middle += 1  # 1
            operation_counter += 4  # 1
            print("array[middle] == K. Count of operation:", operation_counter)
        break
    elif array[middle] < K:  # 1
        middle = (middle + high) // 2  # 3
        operation_counter += 5  # 1
        print("Comparing and calculate middle. Count of operation:", operation_counter)
    elif array[middle] > K:  # 1
        high = middle  # 1
        middle = middle // 2  # 2
        operation_counter += 5  # 1
        print("Comparing and calculate middle. Count of operation:", operation_counter)

print("Count operation w/o sorting: ", operation_counter)
result.sort()
print("Indexes of elements array which equal K: ", result)
