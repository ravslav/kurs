
def main():
    get_date()

def get_date():

    while True:
        date = input("Date: ")
        date = date.split("/")
        month = int(date[0])
        month1 = f"{month:02d}"
        day = int(date[1])
        day1 = f"{day:02d}"
        year = int(date[2])
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month1}-{day1}")
            break
        else:
            continue

main()
