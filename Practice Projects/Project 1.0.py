
# Creates a string titled sentance, then converts this string
# into a list of words using the .split method with a space as the argument.
# also uses the .lower function to convert all the letters into lower case
# this will make it easier when i come to search it the word in a file.
sentance = "This is phenomenal that it works"
sentance = sentance.lower()
sentanceList = sentance.split(" ")

# sorts the list into order using the sorted function.
newlist = sorted(sentanceList, key=len, reverse = True)
# The above part is going to be used later when I am working out what the key is.
# For now, the below part is encrypting it with the key.
# Just change the + to a - to decrypt.

encryptedChars = []
i = 0
key = 5

while(i < len(sentanceList)):
    
    for chars in sentanceList[i]:
                      
        num = ord(chars)
        num += key
        encryptedChars.append(chr(num))
    encryptedChars.append(' ')
    i+=1
        
print " ".join(str(x) for x in encryptedChars) # converts it back into string form.
   
    
# This version is just getting it to ENCRPYT a string of characters.
# It does not handle the letter Z properly though
# If it is Z it will continue on to brackets and stuff

# A note: It is going to be hard to create an if statement for Z
# if I don't know what the key is.

# Probably be best to try and decrypt one with the key
