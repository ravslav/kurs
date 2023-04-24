def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")

def convert(x):
    hours, minutes = x.split(":")
    min_in_h = float(minutes) / 60
    total_t = float(hours) + min_in_h
    return total_t

if __name__ == "__main__":
    main()
