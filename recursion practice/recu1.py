# def printName(s,i):
#     if i ==0:
#         return
#     print(s)
#     i-=1
#     printName(s,i)
# printName("hello",5)



# def printnum(n,i=1):
#     if n<i:
#         return 
#     print(i)
#     i+=1
#     printnum(n,i)
# printnum(5)

# def printrev(n):
#     if n==0:
#         return
#     print(n)
#     printrev(n-1)
# printrev(5)


# def printnum(n):
#     if n==0:
#         return
#     printnum(n-1)
#     print(n)
# printnum(5)


def printrev(i,n):
    if i>n:
        return 
    printrev(i+1,n)
    print(i)
printrev(1,5)

