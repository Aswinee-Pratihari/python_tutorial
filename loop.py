"""
while True:
    n=int(input("what is value of n? "))
    if n>0:
        break;

for i in range(n):
    print("hi "+ str(i+1) );
"""

"""
def main():
    number=getNumber()
    meow(number)

def getNumber():
    while True:
        n=int(input("what is value of n? "))
        if n>0:
            return n;

def meow(n):
    for _ in range(n):
        print("meow")
main()
"""

#LIST/ARRAY
students=["Akash","Harry","Rakesh","Rohan"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1,students[i])