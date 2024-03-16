def main():
    x=int(input("enter your  number"));
    print(f"the square of the number is {square(x)}");


def square(x=0):
    return pow(x,2);


main();