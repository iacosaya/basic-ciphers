#all print statements except the "final" are pointless.

str1 = [[]]
str2 = []
str3 = [[]]
final = ""
word = 0

phrase = [*input("Enter a string (letters a-z, spaces and nothing else): ").lower()]
asnl = input("Enter the key (letter a-z): ").lower()[0]

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
asnlind = alph.index(asnl)

print(phrase)

for letter in phrase:
    #skips whitespaces and instead creates a new list
    if letter != " ":
        letter = alph.index(letter)
        print("Letter index", letter)
        key = (letter - asnlind)
        print("Difference from key", key)
        str1[(word)].append(key)
        str2.append(key)
    else:
        str1.append([])
        word += 1

print(str1)

#range of numbers
phrange = max(str2) - min(str2)
print("Range", phrange)
#length of phrase
phlen = len(str2)
print("Length", phlen, "\n")

word = 0
print("Word", word)
while word <= len(str1) - 1:
    #y is the number which gets modified and x is the position of that number
    for x, y in enumerate(str1[word]):
        print("Index ", x, "Number ", y)
        #adds the range and length to the number (y)
        #can be adjusted to add the squares of the range etc.
        y += phrange + phlen
        str3[(word)].append(y)
        final += str(y) + " "
        if x == len(str1[word]) - 1:
            word += 1
            if word < len(str1):
                print("Word ", word)
                str3.append([])
                final += "/ "
print(str1)
print(str3)
print("Key", asnl)
print("Final result than can be decrypted", final)