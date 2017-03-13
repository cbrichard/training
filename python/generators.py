def counter():
    i=0
    while True:
        i+=1
        return i

a = counter()
print a


# Generator
def counter2():
    i=0
    while True:
        i+=1
        yield i
# This will generate a increment number each time
a = counter2()
print next(a) # Output 1
print next(a) # Output 2
