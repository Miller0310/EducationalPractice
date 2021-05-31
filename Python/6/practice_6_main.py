from practice_6_linked_list import LinkedList
from practice_6_observer import Observer
from practice_6_logger import Logger
from practice_5_strategy import Strategy
from practice_5_generate import Generate
from practice_5_read import Read
from Validator import Validator


logger = Logger("actions.txt")
validator = Validator()
context = Strategy(Generate())
linkedList = LinkedList()

linkedList.eventManager.subscribe(Observer("add", logger.printToFile))
linkedList.eventManager.subscribe(Observer("remove", logger.printToFile))

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
            linkedList = context.generateData(linkedList)
        elif choice == 4:
            print("Enter element's position.")
            pos = validator.integer(input())
            linkedList.Remove(pos)
        elif choice == 5:
            print("Enter from which element.")
            begin = validator.integer(input())
            print("Enter to which element.")
            end = validator.integer(input())
            linkedList.RemoveNodes(begin, end)
        elif choice == 6:
            linkedList.Swap()
        elif choice == 7:
            linkedList.Print()
        elif choice == 8:
            break
    except Exception as e:
        print(e)
