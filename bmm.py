n1=int(input('enter number 1: '))
f=[]
c=[]
n2=int(input('enter number 2: '))

for i in range(1,n1):
    if n1%i==0:
        f.append(i)

for i in range(1,n2):
    if n2%i==0 and i in f:
        c.append(i)

print('bmm= ' , max(c))



   