m1=[[0]*3 for i in range(3)];m2=[[0]*3 for i in range(3)]; m3=[[0]*3 for i in range(3)]
for i in range(3): arr=list(map(int, input().split())); m1[i]=arr.copy()
for i in range(3): arr=list(map(int, input().split())); m2[i]=arr.copy()
for i in range(3):
    for j in range(3):
        summ=0
        for k in range(3):
            summ+=m1[i][k]*m2[k][j]
        m3[i][j]=summ
for i in m3:
    print(i)

# class bank:
#     total=0
#     def __init__(self,name):
#         self.name=name
#         self.bal=0  
#     def credit(self,amt):
#          self.bal+=amt
#          bank.total+=amt
#     def debit(self,amt):
#         self.bal-=amt
#         bank.total-=amt
# b1=bank("naman")
# b2=bank("hero")
# b1.credit(21)
# print(b1.total,b2.total,bank.total)
# b2.debit(10)
# print(b1.total,b2.total,bank.total)
