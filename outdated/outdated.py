
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
"""
def main():
    get_date()

def get_date():
    while True:
        month_list = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

        date = input("Date: ")
        date = date.split()
        month = date[0]
        day = int(date[1])
        day1 = f"{day:02d}"
        year = date[2]
        for m in month_list:
            if m == month:
                x = month_list.index(month)
                print(f"{year}-{x+1}-{day1}")
                return
            else:
                continue
main()
"""


