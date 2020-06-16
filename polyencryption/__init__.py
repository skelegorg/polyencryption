# this file contains the polyalphabetic encryption/decryption algorithms
import secrets


def regenerateKey(length=10):
    # Generate a couple random numbers and save them on different lines
    keyFile = open("key.txt", "w")
    loopHelper = 0
    while(loopHelper < length):
        keyFile.write(str(secrets.randbelow(6)) + '\n')
        loopHelper += 1


def encrypt(fileToEncrypt):
    # Open files
    try:
        keyFileTest = open("key.txt", "r")
        # fix an issue with line 24
        fileExists = True
        keyFileTest.close()
    except FileNotFoundError:
        # if no key file exists, create a key file and start the function over
        regenerateKey()
        encrypt(fileToEncrypt)
    # figure out how many digits to cycle through
    keyCounter = 0
    with open("key.txt", "r") as key:
        for line in key:
            keyCounter += 1
    # if the keyfile exists, open it up
    if(fileExists == True):
        keyFile = open("key.txt", "r")
    # open the file to encrypt
    encryptFile = open(fileToEncrypt, "r")
    # if the keyfile is not empty
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        # Saves the unencrypted file
        encryptArray = []
        for line in encryptFile:
            # save on a line-to-an-index basis
            currentLine = line.strip()
            encryptArray.append(currentLine)
        encryptFile.close()
        # now that the file is saved, empty it out
        encryptFile = open(fileToEncrypt, "w")
        encryptFile.close()
        elemLoopHelper = 0
        keyArray = []
        keySwitcher = 0
        # Populate the keyArray with all the digits of the key
        with open("key.txt", "r") as keyFile:
            for line in keyFile:
                keyLine = line.strip()
                keyArray.append(keyLine)
        # for each line in the password file
        for element in encryptArray:
            # Reset/create a string which holds the current encrypted line
            encryptedLine = ''
            # For each character in each line of the password file
            for char in encryptArray[elemLoopHelper]:
                # Figure out which element of the key is being added
                polyAdd = int(keyArray[keySwitcher])
                # Go through key values and add them to each
                enChar = ord(char) + polyAdd
                # Convert enChar to enCharS
                enCharS = chr(enChar)
                # Add each newly encrypted character to the encryptedLine string
                encryptedLine += enCharS
                # Change the character being read by the polyNumAdd
                keySwitcher += 1
                if (keySwitcher == keyCounter):
                    keySwitcher = 0
            # replace the unencrypted line of the array with the encrypted line
            encryptArray[elemLoopHelper] = encryptedLine
            # Change the slot of the array that is being encrypted
            elemLoopHelper += 1
        with open(fileToEncrypt, "a") as pwf:
            for element in encryptArray:
                pwf.writelines(element + '\n')
    else:
        # No key, so generate one
        regenerateKey()
        # start over
        encrypt(fileToEncrypt)


def decrypt(fileToDecrypt):
    # Open files
    try:
        keyFile = open("key.txt", "r")
    except FileNotFoundError:
        raise FileNotFoundError("no key file was found in the directory")
    # figure out how many digits to cycle through
    keyCounter = 0
    with open("key.txt", "r") as key:
        for line in key:
            keyCounter += 1
    # open the file to decrypt
    decryptFile = open(fileToDecrypt, "r")
    # if the key file was not empty, start the decrypting process
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        # Saves the unencrypted password file
        decryptArray = []
        # populate the decryptArray with on a line-to-an-index basis
        for line in decryptFile:
            currentLine = line.strip()
            decryptArray.append(currentLine)
        decryptFile.close()
        # clear the file
        decryptFile = open(fileToDecrypt, "w")
        decryptFile.close()
        elemLoopHelper = 0
        keyArray = []
        keySwitcher = 0
        # Populate the keyArray with all the digits of the key
        with open("key.txt", "r") as keyFile:
            for line in keyFile:
                keyLine = line.strip()
                keyArray.append(keyLine)
        # for each line in the password file
        for element in decryptArray:
            # Reset/create a string which holds the current encrypted line
            decryptedLine = ''
            # For each character in each line of the password file
            for char in decryptArray[elemLoopHelper]:
                # Figure out which element of the key is being added
                polyAdd = int(keyArray[keySwitcher])
                # Go through key values and add them to each
                deChar = ord(char) - polyAdd
                # Convert deChar to deCharS
                deCharS = chr(deChar)
                # Add each newly decrypted character to the decryptedLine string
                decryptedLine += deCharS
                # Change the character being read by the polyNumAdd
                keySwitcher += 1
                if (keySwitcher == 10):
                    keySwitcher = 0
            decryptArray[elemLoopHelper] = decryptedLine
            # Change the slot of the array that is being encrypted
            elemLoopHelper += 1
        with open(fileToDecrypt, "a") as pwf:
            for element in decryptArray:
                pwf.writelines(element + '\n')
    else:
        raise FileNotFoundError("no key file was found in the directory")
