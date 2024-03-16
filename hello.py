
#remove white spaces from str and capitalize the name#remove white spaces from str and capitalize the name
name=input("what is your name ").strip().title()

#getting the first name
first , last=name.split(" ");  #split returns an array of string with each element separated by space

print(f"hello {first}")  #using variables in a string without concatination

#another method
name=name.split(" ")[0]; #name=firstname


