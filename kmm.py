n1=int(input('enter number 1: '))
n2=int(input('enter number 2: '))
f=[]
c=[]
for i in range(1,100):
    a=n1*(i+1)
    f.append(a)



for j in range(1,100):
    b=n2*(j+1)
    c.append(b)


print('kmm is= ' , min(c))
        


