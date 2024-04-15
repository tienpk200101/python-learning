import random

x = "hello world script"

def myFunction():
    global x
    x = "hello my brother"
    print(x)

def randomNumber():
    print(random.randrange(1, 10))

randomNumber()