import sys
import random

def random_generator(length):
    l1=10**(length-1)
    l2=10**length
    x=random.randint(l1,l2-1)
    guessing(x,length)

def guessing(x,length):
    count=1
    try:
        guess=int(raw_input('Guess a {this} digit number: '.format(this=length)))
        while True:
            if guess<x:
                guess=int(raw_input('Try again. Guess a higher number: '))
                count+=1
            elif guess>x:
                guess=int(raw_input('Try again. Guess a lower number: '))
                count+=1
            else:
                if count==1:
                    print 'Congratulations. You guessed the correct number in 1 try. '
                else:
                    print 'Congratulations. You guessed the correct number in {this} tries'.format(this=count)
                break
    except:
        print 'Need to enter integer values only'

def main():
    print "Let's play the mimsmind0 game. "
    try:
        length=int(sys.argv[1])
        random_generator(length)
    except:
        random_generator(1)


main()