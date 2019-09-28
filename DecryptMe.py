import KeyGetter

sentance = raw_input("Enter the message you wish to decrypt:\n")
print("Finding Key and Decrypting Message...")

sentance = sentance.lower()
sentanceList = sentance.split(" ")
i = 0
decryptedChars = []


key = KeyGetter.getKey(sentance)


def decryptIt(num):

    dNum = -key % 26 + num #works out the numerical pos of alphabet the new char is and adds ascii val
    if (dNum > 122): #if the val is out of ascii alphabet range
        dNum -= 26   #sub 26 to put at correct location 
    decryptedChars.append(chr(dNum))


while(i < len(sentanceList)): #loops through each word
    for char in sentanceList[i]: #loops through each letter of word
        num = ord(char)
        decryptIt(num)

    decryptedChars.append(' ')
    i+=1 #moves on to next word

print("".join(str(x) for x in decryptedChars))
