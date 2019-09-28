
# Creates a string titled sentance, then converts this string
# into a list of words using the .split method with a space as the argument.
# also uses the .lower function to convert all the letters into lower case
# this will make it easier when i come to search it the word in a file.
sentance = "wklv lv dpd}lqj wkdw lw zrunv"
sentance = sentance.lower()
sentanceList = sentance.split(" ")

# sorts the list into order using the sorted function.
# longest word first so more likely to find in dictionary
# as less likely to accidently stumble on a word 
newlist = sorted(sentanceList, key=len, reverse = True)

# I now need to figure out the key.

keyFound = False    
key = 1     
decryptedChars = []     # creates empty list for string to be passed through

with open('myDictionaryTest.txt') as dictionary_file:
   dictionary = dictionary_file.read()


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


# next need to be able to go to the next word if it was unable
# to find the key with the first word. also need it to stop if
# probably when key hits 25 do newlist[1]

# and also need to solve problem of zxy abc etc.
    
