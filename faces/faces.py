def main():
    face = convert(input())
    print(face)
def convert(f):
    f = f.replace(":)","🙂")
    f = f.replace(":(","🙁")
    return f


main()