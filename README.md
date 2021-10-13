# ShiftCipherAlgorithm
This repository highlights the basic shift cipher algorithm that allows users to encrypt and decrypt text. 

In the src code folder, we have a single .py file that is used to encrypt/decrypt the algorithm.

Features of the .py code:
1) Encrypt an inputted text using a chosen key (1 - 25)
2) Decrypt an inputted text using a chosen key (1 - 25)
3) Decrypt an inputted text WITHOUT knowing the chosen key.  If the key is unknown, 
the program will use an exhaustive algorithm that checks every possible decryption and prints them out.

Q: Why must the key be within ranges 1 to 25?
A: In the shift cipher algorithm, we are attempting to shift every letter in the inputted text by the key amount.
For example, given the letter 'A' and the key 2, we would encrypt the letter as 'C' (A - > B - > C)
As a result, there are 25 possible UNIQUE shifts.  Although you can shift more, they would result in the same number as the original 25.
We also don't include 26 as a shift since it would bring us to our original letter (26 letters in the alphabet).

Q: What are some future modifications that can be made to this program?
A: In the future, I'd like to implement a library that can read the text from the exhaustive algorithm that would be able to determine if the decryption was a string of proper words!  Also, I would like to the encryption to maintain its original caps case.  In this simple demonstration, it returns the encryption in only uppercase.  I plan to fix this in the future.

PSUEDOCODE:

encrypt(inputString, shift):
    encryptedText = ""
    for char in inputString:
        if checkifalphabetical(char):
            encryptedText += ord(char) + shift
        else:
            encryptdTexed += char
    return encryptedText

decryptWithKey(inputString, shift):
    decryptedText = ""
    for char in inputString:
        if checkifalphabetical(char):
            encryptedText += ord(char) - shift
        else:
            decryptdTexed += char
    return decryptedText

decryptWithoutKey(inputString):
    for i in range(1, 26):
        oneIteration = ""
        for char in inputString:
            if checkifalphabetical(char):
                oneIteration += ord(char) - i
            else:
                oneIteration += char
        print(oneIteration)
    return True

