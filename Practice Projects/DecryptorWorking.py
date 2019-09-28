key = 4

sentance = "fvmerw tcxlsr xlmrk mw kevfeki"
sentance = sentance.lower()
sentanceList = sentance.split(" ")
i = 0
decryptedChars = []


def decryptIt(num):

    j = 0
    while(j < key):
        num -= 1
        print num
        if num < 97:
            num = 122
        #num -= 1
        j += 1
    decryptedChars.append(chr(num))


while(i < len(sentanceList)):
    for char in sentanceList[i]:
        num = ord(char)
        decryptIt(num)

    decryptedChars.append(' ')
    i+=1
    
    

print "".join(str(x) for x in decryptedChars)



    
# I want it to handle puncuation
# I also want it to be clearer. 
