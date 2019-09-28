# This program calculates the shift of characters (the key) that has been used
# when a message has been decrypted by a substitution cipher.

sentance = "Jmr xli hsk nyqtih sziv xli lihki"
sentance = sentance.lower()
sentanceList = sentance.split(" ")

# sorts the list into order using the sorted function.
# longest word first so more likely to find in dictionary
# as less likely to accidently stumble on a word 
newlist = sorted(sentanceList, key=len, reverse = True)


keyFound = False    
key = 1     
decryptedChars = []     # creates empty list for string to be passed through

# Opens a dictionary file to be scanned for the decrypted words
with open('myDictionary.txt') as dictionary_file:
   dictionary = dictionary_file.read()

x = 0
while(keyFound == False):
    for chars in newlist[0]: # goes through each char of the first word
        num = ord(chars) # turns char to ascii value
        num -= key # adds the current key to it
        decryptedChars.append(chr(num))
        #turns back into chars and adds them to the empty list
        decryptedWord = "".join(str(x) for x in decryptedChars)
        #converts the list into a string to be able to search for
     
    print decryptedWord
    #might have to put a for loop here to search for word in file
    
    if decryptedWord in dictionary:
        #checks if the decryplist string is in the dictionary
        keyFound = True # if yes this will exit loop and print the key value
        print "FOUND!!"
        print "The Key is {0}".format(key)
    else:
           key += 1
           decryptedChars = []
           if key > 26:
               print ("Could not find word")
               break
           # if not, increments key by 1
           # and also clears the list of its current values, making it empty
           # again for processing the next bunch of characters
    x+=1


# next need to be able to go to the next word if it was unable
# to find the key with the first word. also need it to stop if
# probably when key hits 25 do newlist[1]

# and also need to solve problem of zxy abc etc.
    
