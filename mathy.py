def __init__(self):
    pass



def add(num1, num2, *num3):
    if num3 == ():
        num = num1+num2
    else:
        num = __addelse(num1, num2, num3)
    return num



def __addelse(num1, num2, numlist):
    num = num1+num2
    for i in numlist:
        num = num+i
    return num



def subtract(num1, num2):
    return num1-num2



def multiplier(num, size):
    numlist = []
    for i in range(0, size):
        numlist.append = num*i
    return numlist



def divider(num):
    div = 0
    numlist = []
    while True:
        div = div+1
        if div == num:
            break
        else:
            if div%num == 0:
                numlist.append = div/num



def multiply(num1, num2):
    return num*num2



def divise(num1, num2):
    return num1/num2


    
    
