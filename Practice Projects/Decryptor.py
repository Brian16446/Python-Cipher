key = 4

sentance = 'xlmw mw tlirsqirepd'
sentanceList = sentance.split(" ")
i = 0
decryptedChars = []
j = 0

while(i < len(sentanceList)):
    for char in sentanceList[i]:
        num = ord(char)

        if num < 97:
            num = 122
            num -= key
            decryptedChars.append(chr(num))
        else:
            num -= 4
            decryptedChars.append(chr(num))
    decryptedChars.append(' ')
    i+=1
    
    

print " ".join(str(x) for x in decryptedChars)

