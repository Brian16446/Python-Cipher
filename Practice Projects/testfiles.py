with open ('myDictionary.txt', 'r') as dictionary_file:
    dictionary = dictionary_file.read()

    
if 'refrigerator' in dictionary:
    print "This Works"
else:
    print "This doesn't work"
    
