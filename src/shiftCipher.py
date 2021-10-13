# ShiftCipher function
def shiftCipher(string, num):
    # Initialize string to be concatinated with other chars
    encryptedWord = ""
    # Use a for loop to iterate through the inputString
    for i in range(len(string)):
        if string[i].isalpha():
            char = string[i].upper()
            # We subtract by 65 here because 'A' has a unicode value of 65
            # This way, we start from the first possible value 
            # We also have to shift the letter by the given key
            # Hence, we add by the key num
            # We also must maintain the letters within the alphabet, hence the % 26
            encryptedChar = chr((ord(char) + num - 65) % 26 + 65)
            encryptedWord += encryptedChar
        else:
            encryptedWord += string[i]
    # Return end result
    return encryptedWord

#ShiftDecipher function (With Key)
def shiftDecipher(string, num):
    # Initialize string to be concatinated with other chars
    decryptedWord = ""
    # Use a for loop to iterate through the inputString
    for i in range(len(string)):
        # Check if string is alphabetical
        # If so, we would shift the letter by the key amount
        if string[i].isalpha():
            char = string[i].upper()
            # We subtract by 65 here because of the same reason as encrypt
            # The only difference in the solution is that we subtract num, as we
            # are going backwards
            decryptedChar = chr((ord(char) - num - 65) % 26 + 65)
            decryptedWord += decryptedChar
        # If the character isn't an alphabetical character, we would simply
        # concatinate the character to the end of the string
        else:
            decryptedWord += string[i]
    # Return end result
    return decryptedWord

#ShiftDecipher function (Without Key)
def exhaustiveDecrypt(string):
    # Use a for loop to iterate through all 25 possible decryptions
    for i in range(1, 26):
        # Initialize string
        decryptedWord = ""
        # Use a for loop to iterate through the inputString
        for j in range(len(string)):
            # same algorithm as decryption with key, but subbing "num" for i
            if string[j].isalpha():
                char = string[j].upper()
                decryptedChar = chr((ord(char) - i - 65) % 26 + 65)
                decryptedWord += decryptedChar
            else:
                decryptedWord += string[j]
        
        # Return each decryptedWord per iteration 
        print(f'Shift:{i}, {decryptedWord}')
    
    # Confirms all iterations have been tested
    print("All possible cases have been completed!")
    
    pass

# main function
def main():
    # Checks if we would like to encrypt or decrypt
    option = input("Would you like to encrypt or decrypt? (E or D) ")
    while option.upper() != "D" and option.upper() != "E":
        option = input("ERROR: Please enter 'E' to encrypt or 'D' to decrypt: ")
    
    # If encrypting
    # Enter inputString
    # Enter Key
    # Call shiftCipher() function
    if option.upper() == "E":
        text = input("Please enter something to encrypt: ")
        key = int(input("Please enter the value you would like to shift (1 - 25): "))
        while key >= 26 or key <= 0:
            key = int(input("ERROR: Invalid number; Please enter value between 1 and 25: "))
        encryptedText = shiftCipher(text, key)
        print(f'Your original text: {text}')
        print(f'Your encrypted text: {encryptedText}')
    
    # else, we know we're decrypting
    # Enter inputString
    # Ask user if they know the key or not
    # If we do, enter the key and call shiftDecipher() function
    # Else, we skip key input and run exhaustiveDecrypt() function
    else:
        text = input("Please enter something to decrypt: ")
        doYouKnow = input("Do you know the shift key of this text? (Y or N) ")
        while doYouKnow.upper() != "Y" and doYouKnow.upper() != "N":
            doYouKnow = input("ERROR: Please enter 'Y' for Yes or 'N' for No: ")
        if doYouKnow.upper() == "Y":
            key = int(input("Please enter the shift key (1 - 25): "))
            while key >= 26 or key <= 0:
                key = int(input("ERROR: Invalid number; Please enter value between 1 and 25: "))
            decryptedText = shiftDecipher(text, key)
            print(f'Your deciphered text: {decryptedText}')
        else:
            exhaustiveDecrypt(text)
    
    # Ask the user if they would like to continue\
    # If Yes, recursively call the main() function again
    # Else, terminate the program
    wouldContinue = input("Would you like to continue? (Y or N) ")
    while wouldContinue.upper() != "Y" and wouldContinue.upper() != "N":
        wouldContinue = input("ERROR: Please enter 'Y' for Yes or 'N' for No: ")
    if wouldContinue.upper() == "Y":
        main()
    else:
        print("Terminating program...")
        
        
# call main once to start the program
if __name__ == "__main__":
    main()
