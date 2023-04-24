tweet = input("Input: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
for i in tweet:
    if i in vowels:
        tweet = tweet.replace(i,"")
print(f"Output: {tweet}")