def isArmstrong(number):
    N = len(str(number))
    sum = 0
    for i in range(N):
        sum += int(str(number)[i]) ** N
    if sum == number:
        return True
    else:
        return False
