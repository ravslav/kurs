def main():
    name = input("camelCase: ")
    print("snake_case: ", end="")
    for x in name:
        if x.isupper():
            x = x.lower()
            line = "_"
            print(x.replace(x, line + x),end="")
        else:
            print(x,end="")
    print()


main()