# score=int(input("Enter your score "))

#method -1
"""
if(score>90 and score<=100):
    print("Grade A")
elif(score>60 and score<=90 ):
    print("Grade B")
elif(score>100 or score<0):
    print("invalid score")
else:
    print("Grade C")
"""

#method -2
"""
if(90<score<=100):
    print("Grade A")
elif(60<score<=90 ):
    print("Grade B")
elif(score>100 or score<0):
    print("invalid score")
else:
    print("Grade C")
"""


# even odd number
def main():
    x=int(input("enter your number"))
    if(isEven(x)):
        print("number is even")
    else:
        print("number is odd")


def isEven(x):
   # return True if x%2==0 else False ;
    return x%2==0;
main() 