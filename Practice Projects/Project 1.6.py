sentance = "akfjhasldkfjhsfdasf sdkdfjsalasfd sdkflsf lsadkfjsf fvmerw"
sentance = sentance.lower()
sentanceList = sentance.split(" ")

newlist = sorted(sentanceList, key=len, reverse = True)

keyFound = False    
key = 1     
decryptedChars = []

with open('myDictionary.txt') as dictionary_file:
   dictionary = dictionary_file.read()

x = 0
while(x < len(newlist)):
    while(keyFound == False):
        for chars in newlist[x]:
            charNum = ord(chars)
            num = -key%26+charNum
            if num > 122:
                num -= 26
            decryptedChars.append(chr(num))
            decryptedWord = "".join(str(x) for x in decryptedChars)
           
     
        print decryptedWord
    
        if decryptedWord in dictionary:
            keyFound = True
            print "FOUND!!"
            print "The Key is {0}".format(key)
        else:
               key += 1
               decryptedChars = []
               if key > 26:
                   print ("Could not find word in dictionary")
                   key = 1
                   break
    x+=1
