a=int(input('please enter number: '))
sum=0
t=a

while(a!=0):
    r=a%10
    sum=sum+r**3
    a=a//10

if sum==t:
    print('this is armstrong')
else:
    print('this is not armstrong')