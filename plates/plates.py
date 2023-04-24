def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#main function to rule them all!
def is_valid(s):
    if two_letters(s) and length(s) and numbers_middle(s) and periods(s):
        return True

#“All vanity plates must start with at least two letters.”
def two_letters(l):
    l = l[0:2]
    if l.isalpha():
        return True

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def length(d):
    if len(d) >= 2 and len(d) <=6:
        return True

#“Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def numbers_middle(n):
    if n.isalpha():
        return True
    else:
        for i in n:
            if i.isdigit() and i != "0":
                x=n.split(i,1)
                if x[1].isdigit():
                    return True

#“No periods, spaces, or punctuation marks are allowed.”
def periods(p):
    if p.isalnum():
       return True

main()