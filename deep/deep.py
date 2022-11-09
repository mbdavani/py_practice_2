x = input("What is the answer to Life? ")
x = x.lower

def main():
    if x == "42" or x=="i":
        print("Yes")

    else:
        print("No")
        print(x)

main()