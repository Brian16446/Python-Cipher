sentance = "amrwxsr xli hsk jsyklx sjj e fiev"
sentance = sentance.lower()
sentanceList = sentance.split(" ")
newlist = sorted(sentanceList, key=len, reverse = True)

keyFound = False
key = 1
decryptedChars = []
x = 0

with open('myDictionary.txt') as dictionary_file:
    dictionary = dictionary_file.read()

for chars in newlist[x]:
    num = ord(chars)
    for i in range(0, key):
        num -= 1
        if num < 97:
            num = 122
        decryptedChars.append(chr(num))
        decryptedWord = "".join(str(x) for x in decryptedChars)
        
