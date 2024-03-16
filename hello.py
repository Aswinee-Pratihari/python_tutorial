
name=input("what is your name ")

#remove white spaces from str
name=name.strip()

#Capitalize name of user
name=name.capitalize()

#Capitalize first letter of each word
name=name.title()

print("hello " + name)

# print("hello", name,name); #multiple argumrnts

print("hello \"sir\""); #escape charecters (using double quotation inside double quotation)

print(f"hello {name}")  #using variables in a string without concatination

