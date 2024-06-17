#all print statements except the "final" are pointless.

str1 = [[]]
str2 = []
str3 = [[]]
final = ""
word = 0

phrase = input("Enter a coded message: ")
asnl = input("Enter the key: ").lower()[0]

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
asnlind = alph.index(asnl)
phrase = phrase.split()

for x, y in enumerate(phrase):
    if y != "/":
        print("Index ", x, "Number ", y)
        str1[word].append(y)
        str2.append(int(y))
        length = x
    else:
        str1.append([])
        word += 1

print(str1)
phlen = int(len(str2))
print("Length", phlen)
phrange = int(max(str2) - min(str2))
print("Range", phrange)

word = 0
print("Word", word)
while word <= len(str1) - 1:
    #y is the number which gets modified and x is the position of that number
    for x, y in enumerate(str1[word]):
        print("Index ", x, "Number ", y)
        #adds the range and length to the number (y)
        y = int(y) - phrange - phlen
        z = alph[(y + asnlind)]
        str3[(word)].append(y)
        final += str(z)
        if x == len(str1[word]) - 1:
            word += 1
            if word < len(str1):
                print("Word ", word)
                str3.append([])
                final += " "
print(str3)
print('Decoded phrase "', final, '"')