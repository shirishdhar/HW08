#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

def print_hist_old(h):
    for c in h:
        print c, h[c]


def print_hist_new(h):
    for item in sorted(h):
    	print item, h[item]

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

def histogram_new(s):
    d=dict()
    for c in s:
        d[c]=d.get(c,0)+1
    return d

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt') as f:
        a=f.read().replace(',','').replace('.','').replace(':','')
        return [word for word in a.split()]



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
