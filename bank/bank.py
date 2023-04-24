def main():
    greet = input("Greeting: ").strip().lower()
    if greet == "hello" or greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")
main()