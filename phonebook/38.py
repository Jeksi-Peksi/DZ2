# data = open('file.txt', 'a') # здесь указываем режим,в котором будем работать
# data.writelines() # разделителей не будет
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# def SelectAllReadPhoneNumbers():
#     phonebook = readData('C:/Users/JeksiPeksi/Desktop/pythonDZ2/DZ2/phonebook/phonebook.txt')
#     for i in phonebook:
#         print(i)
# def SelectSomethingReadPhoneNumbers():
#     print("SelectSomething 2")

# def readData(fileName):
#     with open(fileName) as f:
#         phonebook = []
#         for line in f:
#             phonebook.append(line.split(','))
#     return phonebook

# def writeData(fileName, phonebook):
#     with open(fileName) as f:
#         f.writelines(phonebook)
#         print("Data added and saved")

# def addPerson(phonebook):
#     print("Entered data: ")
#     number = max(len(phonebook) + 1)
#     surname = str(input("Entered surname: "))
#     firstname = str(input("Entered first name: "))
#     secondname = str(input("Entered second name: "))
#     phonenumber = int(input("Entered telephone number: "))
#     phonebook.append([number, surname, firstname, secondname, phonenumber])
#     writeData('C:/Users/JeksiPeksi/Desktop/pythonDZ2/DZ2/phonebook/phonebook.txt', phonebook)

# print("""Добрый день! 
#         \n [1] -- press for Показать всё 
#         \n [2] -- press for Выбрать 
#         \n [3] -- """)
# while True:
#     try:
#         if (int(input()) == 1):
#             SelectAllReadPhoneNumbers()
#         elif (int(input()) == 2):
#             SelectSomethingReadPhoneNumbers()
#         else:
#             print("Your number out of range. Try again")
#             break
#     except:
#         print("You entered something, but it's not number")


import os

source = ('C:/Users/JeksiPeksi/Desktop/pythonDZ2/DZ2/phonebook/phonebook.txt')

#READ FILE
def readData (fileName):
    with open (fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(','))
    return phoneBook

#WRITE FILE
def writeData (fileName, phoneBook):
    with open (fileName, 'w') as f:
        for i in phoneBook:
            f.write (','.join(i))
        systemMessage(enteredNum)

# ALL SHOW DATABASE  
def selectAllReadPhoneNumber ():
    phoneBook = readData(source)
    for i in phoneBook:
        print (i)

# FIND PERSON 
def selectSomethingReadPhoneNumber ():
    phoneBook = readData(source)
    flag = False
    phoneNumber = str(input("Enter telephone number:"))
    for i in phoneBook:
        if (phoneNumber == str(i[4])):
            print ("ID              :", i[0])
            print ("SURNAME         :", i[1])
            print ("FIRST_NAME      :", i[2])
            print ("SECOND_NAME     :", i[3])
            print ("TELEPHONE_NUMBER:", i[4])
            print ("")
            flag = True
    return flag

# ADD PERSON
def addPerson ():
    phoneBook = readData(source)
    maxID = 0
    for i in phoneBook:
        if (maxID < int(i[0])):
            maxID = int(i[0])
    print ("Enter data:")
    number = str(maxID + 1)
    surname = str(input("Enter surname:"))
    nameFirst = str(input("Enter first name:"))
    nameSecond = str(input("Enter second name:"))
    phoneNumber = str(input("Enter telephone number:"))
    n = ' \n'
    phoneBook.append([number, surname, nameFirst, nameSecond, phoneNumber, n])
    writeData(source, phoneBook)

#EDIT PERSON
def editPerson ():
    phoneBook = readData(source)
    print ("Edit data:")
    flag = selectSomethingReadPhoneNumber ()
    if (flag == True):
        print ("Do you want to change the details of a person?")

        if (answerUserYesOrNo() == 'Y'): 
            print ("Enter ID to edit person:") 
            editID = int(answerUserNumberIndex(phoneBook))
            for i in phoneBook:
                if (editID == int(i[0])):
                    print ("ATTENTION! EDIT PERSON MOD: ON")
                    print ("ID              :", i[0])
                    print ("SURNAME         :", i[1])
                    print ("FIRST_NAME      :", i[2])
                    print ("SECOND_NAME     :", i[3])
                    print ("TELEPHONE_NUMBER:", i[4])

                    oldSurName = i[1]
                    oldFirstName = i[2]
                    oldSecondName = i[3]
                    oldPhoneNumber = i[4]

                    print ("Edit SURNAME ?")
                    newSurName = answerUserYesOrNo()
                    if (newSurName == 'Y'):
                        newSurName = str(input("Enter surname:"))
                    else:
                        newSurName = str(oldSurName)

                    print ("Edit FIRST_NAME ?")
                    newFirstName = answerUserYesOrNo()
                    if (newFirstName == 'Y'):
                        newFirstName = str(input("Enter first name:"))
                    else:
                        newFirstName = str(oldFirstName)

                    print ("Edit SECOND_NAME ?")
                    newSecondName = answerUserYesOrNo()
                    if (newSecondName == 'Y'):
                        newSecondName = str(input("Enter second name:"))
                    else:
                        newSecondName = str(oldSecondName)

                    print ("Edit TELEPHONE_NUMBER ?")
                    newPhoneNumber = answerUserYesOrNo()
                    if (newPhoneNumber == 'Y'):
                        newPhoneNumber = str(input("Enter telephone number:"))
                    else:
                        newPhoneNumber = str(oldPhoneNumber)
                        
                    print ("ID              :", editID)
                    print ("SURNAME         :", oldSurName, "==>", newSurName)
                    print ("FIRST_NAME      :", oldFirstName, "==>", newFirstName)
                    print ("SECOND_NAME     :", oldSecondName, "==>", newSecondName)
                    print ("TELEPHONE_NUMBER:", oldPhoneNumber, "==>", newPhoneNumber)
                    print ("                 Are your sure about that changes?")
                    n = ' \n'
                    if (answerUserYesOrNo() == 'Y'):
                        phoneBook[phoneBook.index(i)] = ([str(editID), newSurName, newFirstName, newSecondName, newPhoneNumber, str(n)])
                        writeData(source, phoneBook)    
                    else:
                        print ("Edit not saved")
        else:
            print ("Edit canceled")          
    return flag
      

def deletePerson ():
    phoneBook = readData(source)
    print ("Delete data:")
    flag = selectSomethingReadPhoneNumber ()
    if (flag == True):
        print ("Do you want to change the details of a person?")
        if (answerUserYesOrNo() == 'Y'): 
            print ("Enter ID to edit person:") 
            editID = int(answerUserNumberIndex(phoneBook))
            for i in phoneBook:
                if (editID == int(i[0])):
                    print ("ATTENTION! DELETE PERSON MOD: ON")
                    print ("ID              :", i[0], "==> DELETE")
                    print ("SURNAME         :", i[1], "==> DELETE")
                    print ("FIRST_NAME      :", i[2], "==> DELETE")
                    print ("SECOND_NAME     :", i[3], "==> DELETE")
                    print ("TELEPHONE_NUMBER:", i[4], "==> DELETE")
                    print ("                 Are your sure about that changes?")
                    if (answerUserYesOrNo() == 'Y'):
                        phoneBook.pop(phoneBook.index(i))
                        writeData(source, phoneBook)   
                    else:
                        print ("Delete not save")
        else:
            print ("Delete canceled")
    return flag   

# Обработка ответа пользователя Yes/No на бесконечке
def answerUserYesOrNo():
    while True:
        answer = str.upper(input("[Y]es or [N]o :"))
        try:
            if (answer == 'Y') or (answer == 'N'):
                return answer
            else:
                print("Your entered no [Y] or [N]. Try again")   
        except:
            print ("You entered something, but it's not number")

# Обработка ответа пользователя Number на бесконечке
def answerUserNumberIndex(phoneBook):
    maxID = 0
    for i in phoneBook:
        if (maxID < int(i[0])):
            maxID = int(i[0])
    while True:
        enteredNum = int(input())
        try:
            if (enteredNum > 0) and (enteredNum <= maxID):
                return enteredNum              
            else:
                print("Your number out of range. Try again")      
        except:
            print ("You entered something, but it's not number")
          
# SYSTEM MESSAGES
def systemMessage(numberMSG):
    if (numberMSG == 2):
        print ("Found person finished")
    elif (numberMSG == 3):
        print ("Data succefull added and saved")
    elif (numberMSG == 4):
        print ("Data succefull edited and saved")
    elif (numberMSG == 5):
        print ("Data succefull deleted. Changes saved")
    elif (numberMSG == 0):
        print ("GOODBYE! COME AGAIN!")
    else:
        print ("Something ERROR. Please contact the developers")


clear = lambda: os.system ('cls')
clear()

print ('''HELLO, USER 
        \n [1] -- press for SHOW ALL 
        \n [2] -- press for SELECT
        \n [3] -- press for ADD DATA
        \n [4] -- press for EDIT DATA
        \n [5] -- press for DELETE DATA
        \n [0] -- press for EXIT
        ''')
while True:
    enteredNum = int(input())
    try:
        if (enteredNum == 1):
            selectAllReadPhoneNumber()
        elif (enteredNum == 2):
            flag = selectSomethingReadPhoneNumber()
            if (flag == True):
                systemMessage(enteredNum)
            else:
                print ("Sorry, not found")
        elif (enteredNum == 3):
            addPerson ()               
        elif (enteredNum == 4):
            flag = editPerson ()
            if (flag != True):
                print ("Sorry, not found")
        elif (enteredNum == 5):
            flag = deletePerson ()
            if (flag != True):
                print ("Sorry, not found")
        elif (enteredNum == 0):
            systemMessage(enteredNum)
            break                
        else:
            print("Your number out of range. Try again")
            
    except:
        print ("You entered something, but it's not number")
