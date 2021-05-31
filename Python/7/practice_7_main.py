from practice_5_linked_list import LinkedList
from practice_5_strategy import Strategy
from practice_5_generate import Generate
from practice_5_read import Read
from Validator import Validator
import threading

validator = Validator()
context = Strategy(Generate())
linkedList1 = LinkedList()
linkedList2 = LinkedList()
lists = [linkedList1, linkedList2]
threads = []
functions = []


def Threads(function, *parameter):
    for i in function:
        t = threading.Thread(target=i, args=parameter)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    threads.clear()
    functions.clear()


while True:
    try:
        print("[1]-Generate with iterator.\n"
              "[2]-Read from file.\n"
              "[3]-Generate data.\n"
              "[4]-Delete element by position.\n"
              "[5]-Delete elements from-to.\n"
              "[6]-Method for work with list.\n"
              "[7]-Print list.\n"
              "[8]-Quit.\n"
              "Enter your choice:", end='')
        choice = validator.integer(input())
        if choice == 1:
            context._strategy = Generate()
        elif choice == 2:
            context._strategy = Read()
        elif choice == 3:
            linkedList1 = context.generateData(linkedList1)
            linkedList2 = context.generateData(linkedList2)
        elif choice == 4:
            print("Enter element's position.")
            pos = validator.integer(input())
            for i in range(len(lists)):
                functions.append(lists[i].Remove)
            Threads(functions, pos)
        elif choice == 5:
            print("Enter from which element.")
            begin = validator.integer(input())
            print("Enter to which element.")
            end = validator.integer(input())
            for i in range(len(lists)):
                functions.append(lists[i].RemoveNodes)
            Threads(functions, begin, end)
        elif choice == 6:
            for i in range(len(lists)):
                functions.append(lists[i].Swap())
            Threads(functions)
        elif choice == 7:
            for i in lists:
                i.Print()
        elif choice == 8:
            break
    except Exception as e:
        print(e)
