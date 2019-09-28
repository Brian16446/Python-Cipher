#Decrypts it with key of 3
#Also works around z
#Ascii number for z is 122
#Ascii number for a is 97
#when DECRYPTING only have to care about a
#when ENCRYPTING have to care about z
#Word is phenomenal.

key = 4

sentance = 'the world can be one together cosmos without hatred'
sentanceList = sentance.split(" ")
i = 0
encryptedChars = []

def encryptIt(num):

    j = 0
    while(j < key):
        num += 1
        if num > 122:
            num = 97
        #num += 1
        j += 1
    encryptedChars.append(chr(num))


while(i < len(sentanceList)):
    for char in sentanceList[i]:
        num = ord(char)
        encryptIt(num)

    encryptedChars.append(' ')
    i+=1
    
    

print "".join(str(x) for x in encryptedChars)


#modulus to get remainder.
#maths is the answer
#probably some mathmatical function that will make it work.
