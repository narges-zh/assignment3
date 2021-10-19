import random

words_bank = ['tree','book','python','nrgs','linux','mac','oslab','windows','java']

#index=random.randint(0,len(words_bank)-1)#-1 chon 8 ta khone bishtar nadarim
#word=words_bank[index]
#or
word=random.choice(words_bank)

joon=7

user_true_chars=[]
print(' _ '*len(word))

while True:

  user_char=input('\nplease enter charactor: ') 


  if user_char in word:
    user_true_chars.append(user_char)
  else:
    joon-=1  
    print('no')

  if joon==0:
      print('game over')
   

  t=0
  for char in word:
      if char in user_true_chars:
        print (char,end=' ')
        t+=1
      else:
        print(' _ ',end=' ')
      
  if t== len(word):
      print('you win')
      break



