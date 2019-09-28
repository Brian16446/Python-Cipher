import Project 

sentance = "fvmerw tcxlsr xlmrk mw kevfeki"
sentance = sentance.lower()
sentanceList = sentance.split(" ")
i = 0
decryptedChars = []


key 

def decryptIt(num):

    dNum = -key % 26 + num
    if dNum > 122:
        dNum -= 26
    decryptedChars.append(chr(dNum))


while(i < len(sentanceList)):
    for char in sentanceList[i]:
        num = ord(char)
        decryptIt(num)

    decryptedChars.append(' ')
    i+=1
    
print "".join(str(x) for x in decryptedChars)
