from random import randint
from practice_3_linked_list import LinkedList

linked_list = LinkedList()

try:
    while True:
        menu = int(input(
            "[1] = Insert random values"
            "\n[2] = Insert your values"
            "\n[3] = Swap"
            "\n[4] = Print"
            "\n[0] = Exit"
            "\nEnter: "))
        if menu == 1:
            N = int(input("Enter size: "))
            for i in range(N):
                linked_list.Insert(randint(10 ** 3, 10 ** 4))
        elif menu == 2:
            array = input("Enter array: ")
            for i in array.split(' '):
                value = int(i)
                if (value >= 10 ** 3) & (value < 10 ** 4):
                    linked_list.Insert(value)
                else:
                    print("Value was less than 1000 or more than 10000 so it was ignored")
        elif menu == 3:
            linked_list.Swap()
        elif menu == 4:
            linked_list.Print()
        elif menu == 0:
            break
except Exception as e:
    print(e)
