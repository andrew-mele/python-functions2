#QUESTION 1 Countdown
def countDown(a):
    count = []
    for a in range (5,-1,-1):
        count.append(a)
        print(count)

countDown(5)

#QUESTION 2 Print & Return

def printAndReturn(a):
    print(a[0])
    return(a[1])

printAndReturn([3,5])

#QUESTION 3 First Plus Length

def firstPlus(a):
    a = a[0] + len(a)
    return a

firstPlus([16,3,6,9,12,15])

#QUESTION 4 Values Greater than Second

def greaterThanSecond(a):
    if len(a)<2:
        return False
    greaterList = []
    for x in a:
        if x > a[1]:
            greaterList.append(x)
    print(len(greaterList))
    return greaterList

greaterThanSecond([6,8,10,2,1,44,19,12,3,7,22])
greaterThanSecond([10])

#QUESTION 5

def thisThat(size,value):
    a = []
    for b in range(size):
        a.append(value)
    return a

thisThat(3,22)
