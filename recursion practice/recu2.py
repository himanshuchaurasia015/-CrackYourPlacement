# sum of n numbers
def sumn(n):
    if n<=0:
        return 0
    return n + sumn(n-1)
print(sumn(5))


# factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
sumn=0
print(fact(5))