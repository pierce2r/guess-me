#!/usr/bin/env python2
#Tool For The Brain
#Author :ABU SAFIAN BLAY

import random

secret= random.randint(1,10)
name= raw_input("Please enter your name:")
print ('Lets play a guess game between 1 to 10. You have only 4 attempts')

for i in range(1,5):
 print "Take a guess:"
 guess = input()
 if guess < secret:
   print('Your guess is too low.')
 elif guess > secret:
   print('Your guess is too high.')
 else:
   break    

if guess == secret: 
    print ('Well done ' + name +'!' ' You won on your ' + str(i)+ ' guess' )

else:
    print ('Sorry! You could not guess me right')
