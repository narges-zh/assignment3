array=[]
array_test=[]
array_len=int(input('please enter len array:'))
for i in range(array_len):
   n=int(input('please enter number of array:'))
   array.appen(n)
   array_test.append(n)

array_test.sort()
if array==array_test:
    print('is sort')
else:
    print('is not sort')