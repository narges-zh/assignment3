import random

array_len = int(input('please enter len of array: '))
array=[]

arrays = random.randint(0,10)

while array_len>0 :
    if arrays in array :
        arrays = random.randint(0,10)
    else:
        array.append(arrays)
        array_len-=1

print('youre random array is:' , array)