print ("Hello World")
print("Please enter the term (with #):")
s = input()
with open("search.txt", "r") as f:       
    words = list(map(str.strip, f.readlines()))
    try: 
        text=words[words.index(s) + 1]
        print(text)
    except:
        print("Sorry the word is not found.")
