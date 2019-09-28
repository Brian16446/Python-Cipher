#Decrypts it with key of 3
#Also works around z
#Ascii number for z is 122
#Ascii number for a is 97
#when DECRYPTING only have to care about a
#when ENCRYPTING have to care about z
#Word is phenomenal.

key = 9

sentance = 'Fin the dog jumped over the hedge'
sentanceList = sentance.split(" ")
i = 0
encryptedChars = []

while(i < len(sentanceList)):
    for char in sentanceList[i]:
        num = ord(char)
        num += key
        print num
        if num >= 122:
            num = 97
            encryptedChars.append(chr(num))
        else:
            encryptedChars.append(chr(num))
    encryptedChars.append(' ')
    i+=1

        

encryptedString = "".join(str(x) for x in encryptedChars)
print encryptedString


#modulus to get remainder.
#maths is the answer
#probably some mathmatical function that will make it work.
