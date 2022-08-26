import random
from re import X
import rlcompleter
import math
#rn is random number, rg is random guess, rgg is 50 so that it starts in the middle before it moves, 
# *comment below is what I attempted but I couldn't get a 100% success rate with anything I tried, comment or no, so this seemed like the easiest solution- Now it just guesses any number under 50 if the random number is under 50 and it guesses any number over 50 if the random number is over 50
# I made it add a number between 1-10 randomly if 50 is less than the random number and it subtracts a random number from 1-10 if 50 is more than the random number

rn =random.randint(1,100)
print('the random number is',rn)

def rg():
    
    rgg = 50
    count = 0
   

    while rgg!=rn:

        if rgg>rn:
            print('Guessed too high, guessed',rgg)
            rgg = random.randint(1,49)
            count+=1
        if rgg<rn:
            print('Guessed too low, guessed',rgg)
            rgg = random.randint(51,100)
            count+=1
        if rgg==rn:
            print ('Finally guessed',rn,'after',count, 'tries')
            break
        continue
     
   
rg()
