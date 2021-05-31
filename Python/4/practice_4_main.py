from practice_4_generator import generator
from practice_4_iterator import Iterator

iter = Iterator()
gen = generator()
array = []
try:
    while True:
        menu = int(input("[1] - Iterator"
                         "\n[2] - Generator"
                         "\n[3] - Print"
                         "\n[0] - Quit"
                         "\nEnter: "))
        if menu == 1:
            N = int(input("Enter size: "))
            for i in range(N):
                array.append(next(iter))
        elif menu == 2:
            N = int(input("Enter size: "))
            for i in range(N):
                array.append(next(gen))
        elif menu == 3:
            print(array)
        else:
            break
except Exception as e:
    print(e)
