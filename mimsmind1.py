import sys
import random

def random_generator(length):
    l2=10**length
    x=random.randint(0,l2-1)
    guessing(str(x),length)

def guessing(x,length):
    count=0
    maxrounds=(2**length)+length
    print "Let's play the mimsmind0 game. You have {this} guesses.".format(this=maxrounds)
    guess=(raw_input('Guess a {this} digit number: '.format(this=length)))

    while (count<=maxrounds):
        try:
            int(guess)
            if len(guess)!=length:
                1/0

        except:
            guess=raw_input('Invalid Input. Try again: ')
        else:
            while guess!=x:
                count1=0
                count2=0
                for i in range(0,length):
                    if guess[i]==x[i]:
                        count1+=1
                for i in range(0,length):
                    if (guess[i] in x) and (guess[i]!=x[i]):
                        count2+=1
                count+=1
                guess=(raw_input('{this} bull(s), {this1} cow(s). Try again: '.format(this=count1,this1=count2)))
            count+=1
            print 'Yayyyy {this} tries'.format(this=count)
            break
    if guess!=x:
        print 'Sorry {this} tries over'.format(this=maxrounds)

def main():
    try:
        length=int(sys.argv[1])
        random_generator(length)
    except:
        random_generator(3)


main()