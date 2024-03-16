def main():
    print(hello());
    name=input("what is your name").title();
    print(hello(name));


def hello(name="world"):
    return(f"hello {name}")

main()
# function def needs to be on top for them to be called afterwards

# for this to change we can wrap the logic of our program in a main funtion and then define the functions afterwards

