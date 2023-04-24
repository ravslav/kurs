def main():
    m = int(input("m: "))
    print("E: ", calc(m))

def calc(mass):
    return mass * 300000000**2

main()