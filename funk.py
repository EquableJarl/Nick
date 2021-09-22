import vars
import os
import time

def getSequence():
    x = False
    while x == False:
        seq = input("Please pass in a number sequence: ")
        if seq.isnumeric() == True:
            return seq
        else:
            print("Please provide a valid numeric sequence")


def getPath():
    x = False
    while x == False:
        filePath = input("Please give me the location of the file :")
        try:
            if os.path.exists(filePath) == True:
                return filePath
            else:
                print("This file doesn't exist...")
        except:
            print("This file does not exist please try again.")


def getText(path):
    with open(path) as f:
        return f.read()


def convertMessage(message):
    numbers = []
    for letter in message:
        number = ord(letter)
        numbers.append(number)
    return numbers


def transformMessage(message, seq, deMode):
    count = 0
    transformedMessage = []
    for number in message:
        if count < len(seq):
            count = count
        else: 
            count = 0 

        if deMode == True:
            newNum = number - int(seq[count])
        else: 
            newNum = number + int(seq[count])
        transformedMessage.append(newNum)
        count = count + 1
    return transformedMessage


def encryptMessage(message):
    encryptedMessage = "".join([chr(c) for c in message])
    return encryptedMessage


def chooseMethod():
    while True:
        choice = input(vars.howTo)
        if choice.isnumeric():
            if int(choice) in range(1, 4):
                if choice == "1":
                    encryptData()
                elif choice == "2":
                    decryptData()
                else: 
                    print("Thanks for playing... Goodbye")
                    time.sleep(3)
                    vars.isAlive = False
                    return
            else: 
                print("This is not a vaild selection number")
        else:
            print("Please give a valid option")

def saveFile(textData, mode):
    runMode = ""
    if mode == True:
        runMode = "encrypt"
    else:
        runMode ="decrypt"
    timestr = time.strftime("%Y%m%d-%H%M%S")
    dir = os.getcwd()
    filename = dir + "/" + "AlcRytion-" + runMode + timestr
    f = open(filename, 'a+')  
    f.write(textData)
    f.close()
    print("You file has been stored here : " + filename)
    time.sleep(5)

def encryptData():
    seq = getSequence()
    path = getPath()
    text = getText(path)
    numMessage = convertMessage(text)
    transMessage = transformMessage(numMessage, seq, False)
    encrpytedMessage = encryptMessage(transMessage)
    saveFile(encrpytedMessage, True)


def decryptData():
    seq = getSequence()
    path = getPath()
    text = getText(path)
    numMessage = convertMessage(text)
    transMessage = transformMessage(numMessage, seq, True)
    encrpytedMessage = encryptMessage(transMessage)
    saveFile(encrpytedMessage, False)



