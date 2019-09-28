def getKey(sentance):
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
                if num > 122: #When the number will no longer be a alphabetic character in ascii table
                    num -= 26
                decryptedChars.append(chr(num))
                decryptedWord = "".join(str(x) for x in decryptedChars)
               
         
            print decryptedWord
        
            if decryptedWord in dictionary: #Searches for the word in dictionary
                keyFound = True
                print "FOUND!!"
                print "The Key is {0}".format(key)
            else:   #Adds 1 to the key and wipes the list
                   key += 1
                   decryptedChars = []
                   if key > 26: #So as to not repeat forever
                       print ("Could not find word in dictionary")
                       key = 1 #resets the key to 1 ready for the process to repeat for next word
                       break
        x+=1

    return key
