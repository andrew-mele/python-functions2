#QUESTION 1 Countdown
"""Countdown - Create a function that accepts a number as an input. 
#Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)."""
def countDown(a):
    count = []
    for a in range (5,-1,-1):
        count.append(a)
        print(count)

countDown(5)

#QUESTION 2 Print & Return
#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def printAndReturn(a):
    print(a[0])
    return(a[1])

printAndReturn([3,5])

#QUESTION 3 First Plus Length
#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def firstPlus(a):
    a = a[0] + len(a)
    return a

firstPlus([16,3,6,9,12,15])

#QUESTION 4 Values Greater than Second
"""Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False"""

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
"""Write a function that accepts two integers as parameters: size and value. 
The function should create and return a list whose length is equal to the given size, and whose values are all the given value."""

def thisThat(size,value):
    a = []
    for b in range(size):
        a.append(value)
    return a

thisThat(3,22)
