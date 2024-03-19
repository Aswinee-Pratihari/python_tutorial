from random import choice,randint,shuffle
from statistics import mean
from sys import argv
import sys

coin=choice(["tail","heads"])
number=randint(1,5)
#print(number)

cards=["jack","queen","king"]
shuffle(cards)
#for card in cards:
#    print(card)

marks=mean([100,80])
#print(marks)

"""
try:
    print("hello, my name is ",argv[1])
except IndexError:
    print("Pls enter your name")
"""


if len(argv)<2:
    sys.exit(" too few arguments")
elif len(argv)>2:
    sys.exit("too many arguments")


print("hello, my name is ",argv[1]) 

