This program will take in a message that has been encrypted with a simple substitution cipher, such as a caeser cipher or ROT 13.

It will brute force the key and return both the key value and the decrypted message.

It does this by looking at each word individually and searching a dictionary file of around 420k words to see if it is a valid word. If nothing is found it adds 1 to the key and keeps doing this until the key hits 26. If it is unsuccessful in finding a match, it will then move on to the next word in the message and the process will repeat until all words have been searched, or a match is found. 

It also sorts the message into order starting with the largest word first so to reduce the chances of accidentally stumbling on a word. Typically, the first word is only searched as a match is usually found.

Encrypted sentances to try (feel free to add your own):

huk fvb ybu huk fvb ybu av jhajo bw dpao aol zbu iba paz zpurpun 
sejopkj pda zkc fqilaz kran pda dazca
agf ar ftq nxgq mzp uzfa ftq nxmow
xli asvphw ger fi sri xskixliv gswqsw amxlsyx lexvih