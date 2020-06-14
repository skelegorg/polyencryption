# this file contains the polyalphabetic encryption/decryption algorithms
import secrets


def regenerateKey(length=10):
    # Generate a couple random numbers and save them on different lines
    keyFile = open("key.txt", "w")
    loopHelper = 0
    while(loopHelper < 5):
        keyFile.write(str(secrets.randbelow(length)) + '\n')
        loopHelper += 1


def encrypt(fileToEncrypt):
    # Open files
    keyFile = open("key.txt", "r")
    encryptFile = open(fileToEncrypt, "r")
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        # Saves the unencrypted password file
        encryptArray = []
        for line in encryptFile:
            currentLine = line.strip()
            encryptArray.append(currentLine)
        encryptFile.close()
        encryptFile = open(fileToEncrypt, "w")
        encryptFile.close()
        elemLoopHelper = 0
        keyArray = []
        keySwitcher = 0
        # Populate the keyArray with all 5 digits of the key
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
                # Change the line being read by the polyNumAdd
                keySwitcher += 1
                if (keySwitcher == 5):
                    keySwitcher = 0
            encryptArray[elemLoopHelper] = encryptedLine
            # Change the slot of the array that is being encrypted
            elemLoopHelper += 1
        with open(fileToEncrypt, "a") as pwf:
            for element in encryptArray:
                pwf.writelines(element + '\n')
        print("Encrypted data")
    else:
        # No key, so generate one
        regenerateKey()
        encrypt(fileToEncrypt)


def decrypt(fileToDecrypt):
    # Open files
    keyFile = open("key.txt", "r")
    encryptFile = open(fileToDecrypt, "r")
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        # Saves the unencrypted password file
        encryptArray = []
        for line in encryptFile:
            currentLine = line.strip()
            encryptArray.append(currentLine)
        encryptFile.close()
        encryptFile = open(fileToDecrypt, "w")
        encryptFile.close()
        elemLoopHelper = 0
        keyArray = []
        keySwitcher = 0
        # Populate the keyArray with all 5 digits of the key
        with open("key.txt", "r") as keyFile:
            for line in keyFile:
                keyLine = line.strip()
                keyArray.append(keyLine)
        # for each line in the password file
        for element in encryptArray:
            # Reset/create a string which holds the current encrypted line
            decryptedLine = ''
            # For each character in each line of the password file
            for char in encryptArray[elemLoopHelper]:
                # Figure out which element of the key is being added
                polyAdd = int(keyArray[keySwitcher])
                # Go through key values and add them to each
                deChar = ord(char) - polyAdd
                # Convert enChar to enCharS
                deCharS = chr(deChar)
                # Add each newly encrypted character to the encryptedLine string
                decryptedLine += deCharS
                # Change the line being read by the polyNumAdd
                keySwitcher += 1
                if (keySwitcher == 5):
                    keySwitcher = 0
            encryptArray[elemLoopHelper] = decryptedLine
            # Change the slot of the array that is being encrypted
            elemLoopHelper += 1
        with open(fileToDecrypt, "a") as pwf:
            for element in encryptArray:
                pwf.writelines(element + '\n')
        print("Decrypted data")
    else:
        print("Key not detected")
