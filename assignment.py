#Assignment-1

def main():
    #findAge()
   # fullName()
   #findArea()
    #findChange()
    #tileCost()
    #binaryRep()
    #showAddress()
    #stringSlice()
    #stringReplace()
    areaWithFunction()
# 1. age
def findAge():
    birthYear=int(input("In which year were you born ?"));
    presentYear =2024;
    print(f"your age is {presentYear-birthYear}");


# 2. print name
def fullName():
    firstName=str(input("Enter your first name ").strip().capitalize())
    middleName= str(input("Enter your middle name ").strip().capitalize())
    lastName= str(input("Enter your last name ").strip().capitalize())

    print ("your name is",firstName,middleName,lastName);


# 3 findArea
def findArea():
    length=float(input("enter length of field"))
    width=float(input("enter width of field"))

    area=round(length*width,2);
    print(f"the area of field is {area}")

# 4 findChange
def findChange():
    singlePacket = 1.49;
    totalPackets = 10;
    totalMoney=20;
    
    totalCost=singlePacket * totalPackets
    print(f"the change amount is {round(totalMoney-totalCost)}")

def tileCost():
    tileLength= 5.5
    costPerSqrFeet= 500
    print(f"the total area is {pow(tileLength,2)}")
    totalCost = pow(tileLength,2) * costPerSqrFeet;
    print(f"the total cost is {totalCost}")

def binaryRep():
    print(f"the binary number is {format(17,'b')}")

def showAddress():
    city=input("Enter city name ").capitalize();
    state=input("enter name of state ").capitalize()
    country =input("enter name of country ").capitalize()

    print(f"City:- {city} \n State:- {state} \n Country:- {country}")

def stringSlice():
    string="Earth revolves around sun"
    print(string[6:14])
    print(string[-10:])
    
def stringReplace():
    string="Maine 200 apple khae"
    string= string.replace("200","10").replace("apple","samosa")
    print(string)
main()
