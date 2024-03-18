#dict

students={"Akash":"Green",
          "Harry":"Red",
          "Rakesh":"Purple","Rohan":"White"}

house=["Green","Red","Purple","White"]

print(students["Rakesh"])

for student in students:
   # print(student) #give all th keys
    print(student,students[student],sep=",")


#dictionary within a list 
students=[
    {
        "name":"Akash",
        "House":"Green",
        "class":"6"
    },
    {
        "name":"Rahul",
        "House":"Red",
        "class":"8"
    },
    {
        "name":"Rajesh",
        "House":"White",
        "class":"7"
    },
    {
        "name":"Mehul",
        "House":None,
        "class":"10"
    },
    
]

for student in students:
    print(student["name"],student["House"],student["class"] ,sep=",")


#printing a 2d matrix

# method-1
#for each row in matrix 
for i in range(3):
        # for each column ->
        for j in range(3):
                print("#",end="")
        print()


#method-2
for i in range(3):
        print("*"*3)    