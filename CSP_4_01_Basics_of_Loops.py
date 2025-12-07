#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
    answer=""
    for num in range (1,n+1):
         if num%2 != 0 :
            answer=answer+str(num)+" "
    return(answer[0:len(answer)-1])
"""
Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
 example oddNumbers(5) -> "1 3 5"
 example oddNumbers(8) -> "1 3 5 7"
 example oddNumbers(-8) -> ""
"""


def backwards(n)-> int:
    answer2=""
    num2=n
    while num2 in range (1, n+1):
        answer2=answer2+str(num2)+" "
        num2=num2-1
    return (answer2[0:len(answer2)-1])
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """


import random
def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    x = random.randint(1, 10)
    tries = 0
    while x != 10:
        print(x)
        x = random.randint(1, 10)
        tries=tries+1
    if x==10:
        print(x)
        tries=tries+1
    print(f"it took {tries} tries to get a 10")
randomRepeating()
def randomRange(n):
    """
        Generate a random number from 1 to 100 n number of times. Then after that is
        done print out what the highest number and the lowers number was from the rolled numbers.
        NOTE: Given randomness no test for this question
        :param n:
        :return:
        """
    x=random.randint(1,100)
    max=x
    min=x
    while n>1:
        gen = random.randint(1, 100)
        n=n-1
        if gen>x or gen==x:
            max=gen
        elif gen<x or gen==x:
            min=gen
    print (min, max)
randomRange(5)

def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    answer=""
    n=len(word)-1
    while n>-1:
        answer = answer + word[n]
        n=n-1
    return answer
def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    answer=""
    fb=1
    for fb in range(1,n+1):
        if fb%3==0 and fb%5==0:
            answer=answer+"fizzbuzz "
        elif fb%3==0:
            answer=answer+"fizz "
        elif fb%5==0:
            answer=answer+"buzz "
        else:
            answer=answer + str(fb)+" "
        fb=fb+1
    return (answer[0:len(answer) - 1])


def collatz(n):

    collatzanswer=str(n) + " "
    while n != 1:
        if n%2==0:
            n=n/2
            collatzanswer=collatzanswer + str(int(n)) + " "
        elif n%2==1:
            n=(3*n)+1
            collatzanswer = collatzanswer + str(int(n)) + " "
    return collatzanswer[0:len(collatzanswer)-1]

def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    fibans="0 1 "
    num1=0
    num2=1
    while n>2:
        fibans=fibans+str(num1+num2) + " "
        tempnum=num2
        num2=num1+num2
        num1=tempnum
        n=n-1
    return fibans[0:len(fibans)-1]
print(fibonacci(300))