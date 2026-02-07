# imports 
import math
import random
import re
import time
from string import ascii_lowercase
from string import ascii_uppercase

# variables
goBack = ["go back", "back", "Back", "Go Back", "Go back"]
YES = ['y','Yes','Y','yes']
NO = ['n'or'N'or'No'or'no']

# makes user input correct value 
def yOrN(userInput):
    while True:
        if userInput in YES or userInput in NO:
            break
        else:
            userInput = input("Please input a correct value, y or n \n>")
            continue

# function used to go back to the start of another function
def toStartOfFunction(function, functionInfo): 
    function(*functionInfo) # needs to have all function information backed into a tuple

# removes what is within brackets in a string 
def removeBrackets(test_str):
    # define varaibles
    ret = ''
    skip1c = 0
    skip2c = 0
    skip3c = 0
    # takes characters from input
    for i in test_str:
        # determines amount of start brackets and adds one for every start bracket
        if i == '[':
            skip1c = skip1c + 1
        elif i == '(':
            skip2c = skip2c + 1
        elif i == '{':
            skip3c = skip3c + 1
        # determines amount of end brackets, and removes one for every end bracket
        elif i == ']' and skip1c > 0:
            skip1c = skip1c - 1
        elif i == ')' and skip2c > 0:
            skip2c = skip2c - 1
        elif i == '}' and skip3c > 0:
            skip3c = skip3c - 1
        # once all brackets are closed, removes what is within the bracket
        elif skip1c == 0 and skip2c == 0 and skip3c == 0:
            ret = ret + i
    # returns final string, with all information within bracket removed 
    return ret

# removes what is within brackets in a string, removes notImportant information, converts string to lowercase
def checkNotImportant(Input):
    # not important characters 
    notImportant = {',': '','.': '','"': '',"'": '','!': '','?': '','=': '','+': '','_': '','-': '','*': '','$': '','#': '','@': '','%': '','^': '','~': '','`': '','/': '',';': '',':': '','<': '','>': '','(': '',')': '','[': '',']': '','{': '','}': ''}
    # determines if input is in a list or not 
    whatIsWhat = type(Input)
    if whatIsWhat != list:
        Input = [Input]
    # check used to determine if any notImportant characters are in Input
    check = []
    check = check + Input
    checkSplit = []
    counter = -1
    # check is split into list, containing individual characters 
    while True:
        counter = counter + 1
        if counter == len(check):
            break
        for letter in str(check[counter]):
            checkSplit.append(letter)

    # new input that will be returned 
    newInput = []
    counter = -1
    # splits the list up with ¶ seperating each list element
    while True:
        counter = counter + 1
        if counter == len(Input):
            break
        for letter in str(Input[counter]):
            newInput.append(letter)
        newInput.append("¶")

    # joins list into one string
    newInput = ''.join(newInput)
    
    # removes any brackets with information inside 
    newInput = removeBrackets(newInput)
    
    # removes all not important information
    for key, value in notImportant.items():
        newInput = newInput.replace(key, value)
    

    # converts list back into list containing individual characters 
    newInput = list(newInput)
    
    # makes string characters into lowercase 
    for words in range(len(newInput)):
        newInput[words] = newInput[words].lower()
        

    # makes list into one whole string
    newInput = ''.join(newInput)

    # seperates string into list by ¶, into original arrangement
    newInput = list(newInput.split("¶"))

    # removes last empty string from list
    del newInput[-1]

    # remove all extra spaces 
    counter = 0
    while counter < len(newInput):
        if not newInput[counter] or re.search('^\s*$', newInput[counter]):
            counter = counter + 1
        else:
            newInput[counter] = ' '.join(newInput[counter].split())
            counter = counter + 1

    # if originaly a user input, needs to be converted back into a string to be checked against a list, i will no this if original input was not a list
    if whatIsWhat != list:
        newInput = ''.join(newInput)
    
    # returns the new input 
    return newInput

# determines if input is a number or word, if word converts to number only if an actual number word, otherwise returns -1
def checkIsDigit(Input): 
    if Input.strip().isdigit():
        # if number
        return int(Input)

    else:
        # if string converts string to number
        return int(text2int(Input))

# converts string to numbers
def text2int(textNum,numWords={}): 
    if not numWords:
        # unit words
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        # tenths words
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        # scale words, meaning how much it is 
        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        # last numbers
        numWords["and"] = (1, 0)
        for idx, word in enumerate(units):    numWords[word] = (1, idx)
        for idx, word in enumerate(tens):     numWords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numWords[word] = (10 ** (idx * 3 or 2), 0)


    current = result = 0
    for word in textNum.split():
        # if word is not a number return -1
        if word not in numWords:
            return -1

        # determines scale, actual number 
        scale, increment = numWords[word]
        current = current * scale + increment
        if scale > 100:
            result = result + current
            current = 0

    # return number 
    return result + current

# stop watch, to time how long it takes
def timeConvert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Your time was, {0}:{1}:{2}".format(int(hours),int(mins),int(sec)) + " to match all your flashcards (in formate of Hours:Minutes:Seconds)\n")    

# prints list for flashcards to match up
def printMatchOptions(answerKeyChecker, listLeftColumnLetters, shuffledList1, listRightColumnLetters, shuffledList2):
    counter = -1
    while True:
        counter = counter + 1
        if counter >= len(answerKeyChecker):
            break
        print(str(listLeftColumnLetters[counter]) + ". " + str(shuffledList1[counter]) + "          " + str(listRightColumnLetters[counter]) + ". " + str(shuffledList2[counter]))
        continue

# start of program
def start():
    while True:
        # find if creating subject or accessing subject
        SubjectChoice = input("\n1. View subjects, \n2. Create New Subject, \n3. Create new flashcard set or \n4. Add flashcards to existing set \n>")
        # if input below go to readsubject
        if SubjectChoice == "view subjects" or SubjectChoice == "subject" or SubjectChoice == "Subject" or SubjectChoice == "Subjects" or SubjectChoice == "subjects" or SubjectChoice == "view" or SubjectChoice == "View" or SubjectChoice == "View subject" or SubjectChoice == '1' or SubjectChoice == '1.':
            readSubject()
        
        # if input below go to 
        elif SubjectChoice == "create new subject" or SubjectChoice == "Create New Subject" or SubjectChoice == "create" or SubjectChoice == "Create" or SubjectChoice == "New" or SubjectChoice == "new" or SubjectChoice == '2' or SubjectChoice == '2.':
            createNewSubject()

        # if user wants to add new flashcard set to existing subjects
        elif SubjectChoice == 'Create new flashcard set' or SubjectChoice == 'new flashcard' or SubjectChoice == "New flashcard" or SubjectChoice == 'create new flashcard set' or SubjectChoice == 'set' or SubjectChoice == 'Set' or SubjectChoice == '3' or SubjectChoice == '3.':
            addFlashcardSet()

        # if user wants to add flashcards to existing sets 
        elif SubjectChoice == 'Add flashcards' or SubjectChoice == 'add flashcards' or SubjectChoice == 'add flashcard' or SubjectChoice == 'Add flashcard' or SubjectChoice == '4' or SubjectChoice == '4.':
            addFlashcard()

        else:
            print('Please input a correct value')
            continue

def readSubject():
    while True:
        with open('subjects.txt','r') as readingSubject:

            # converts subject file into string by reading it 
            readSubjects = readingSubject.read()

            # converts subject file into list 
            subjectList = readSubjects.split('\n')

            # prints options of subjects user selects subject
            userChosenSubject = input("\nSelect subject below or go back: \n" + readSubjects + '>')
            
            if userChosenSubject in goBack:
                # goes to start
                readingSubject.close()
                start()
                    
            # if input is equal to option in subject list then go to flashcardSet             
            elif userChosenSubject in subjectList:
                readingSubject.close()
                getFlashcards(userChosenSubject)
                    
            # if input not in subject list then repeat loop
            else:
                print("Please input a correct value")
                readingSubject.close()
                continue

def createNewSubject():                 
    # user choosen to create new subject       
        while True:
            userNewSubjectName = input("Input the name of your subject, please input \n correctly as this can not be changed later \n or go back:\n>")
            # if entered back, goes to start
            if userNewSubjectName in goBack:
                start()
            # entered anything else, continues making new flashcard set
            else:
                # writes user created subject name into subject file to be accessed later 
                with open('subjects.txt','a') as subjectsFile:
                    subjectsFile.write(userNewSubjectName + '\n')
                    subjectsFile.close()
                createFlashcard(userNewSubjectName)

def createFlashcard(userNewSubjectName):
    while True:
        userNewFlashcardName = input("Input the name of your flashcard set, \nplease input correctly as this can not be changed later \n or go back: \n>")
        # if entered back, goes to start
        if userNewFlashcardName in goBack:
            createNewSubject()
                 
        # entered anything else uses that value as the name of the flashcard set
        else:
            
            # creates the new subject, and writes the name of flashcard set in the file
            with open(userNewSubjectName + ".txt","a") as newSubjectFile:
                newSubjectFile.write(userNewFlashcardName + "\n")
                newSubjectFile.close()

            # continues looping to create new flashcards 
            while True:
                # user enters flashcard terms and definitions
                userNewTerm = input('Enter the term of this flashcard\n>')
                userNewDef = input('Input the definition of that term\n>')
                        
                # creating flashcard terms and definitions for that set
                with open(userNewFlashcardName + 'Term.txt','a') as newTermFile:
                    newTermFile.write(userNewTerm + '\n')
                    newTermFile.close()

                with open(userNewFlashcardName + 'Def.txt','a') as newDefFile:
                    newDefFile.write(userNewDef + '\n')
                    newDefFile.close()

                    # determines if you make another flashcard
                    continueEnteringFlashcards = input('\nDo you want to add another flashcard, y or n:\n>')
                    yOrN(continueEnteringFlashcards)
                    if continueEnteringFlashcards in YES:
                        continue
                    elif continueEnteringFlashcards in NO:

                        # determines if you make another flashcard set 
                        continueFlashcard = input('\nDo you wish to continue making another flashcard set, y or n \n>')
                        yOrN(continueFlashcard)
                        if continueFlashcard in YES:
                            # makes another flashcard set
                            break
                        elif continueFlashcard in NO:
                            start()
        # makes another flashcard set 
        continue

# create another flashcard set in a existing subject
def addFlashcardSet():
    while True:
        with open('subjects.txt','r') as readingSubject:

            # converts subject file into string by reading it 
            readSubjects = readingSubject.read()

            # converts subject file into list 
            subjectList = readSubjects.split('\n')

            # prints options of subjects user selects subject
            userChosenSubject = input("\nSelect subject below or go back: \n" + readSubjects + '>')
            
            if userChosenSubject in goBack:
                # goes to start
                readingSubject.close()
                start()
                    
            # if input is equal to option in subject list then go to flashcardSet             
            elif userChosenSubject in subjectList:
                readingSubject.close()
                createFlashcard(userChosenSubject)
                    
            # if input not in subject list then repeat loop
            else:
                print("Please input a correct value")
                readingSubject.close()
                continue

def addFlashcard():
    while True:
        with open('subjects.txt','r') as readingSubject:

            # converts subject file into a string by reading it 
            readSubjects = readingSubject.read()

            # converts subject file into list 
            subjectList = readSubjects.split('\n')

            # prints options of subjects user selects subject
            userChosenSubject = input("\nSelect subject below or go back: \n" + readSubjects + '>')
            
            if userChosenSubject in goBack:
                # goes to start
                readingSubject.close()
                start()
                    
            # if input is equal to option in subject list then go to flashcardSet             
            elif userChosenSubject in subjectList:
                readingSubject.close()
                with open(userChosenSubject + '.txt') as flashcardSets:
                    # converts flashcardset file into a string by reading it 
                    readFlashcardSets = flashcardSets.read()

                    # converts flashcard set file into list 
                    flashcardList = readFlashcardSets.split('\n')
                    # removes last value, because its blank
                    del flashcardList[-1]

                    # asks user what flashcard set they would like to add flashcards to
                    userChosenFlashcardSet = input('\nPlease select your flashcard sets below \nor go back: \n' + readFlashcardSets + ">")
                    if userChosenFlashcardSet in goBack:
                        flashcardSets.close()
                        start()
             
                    # if user input is in the list of flashcard sets continue below
                    elif userChosenFlashcardSet in flashcardList:
                        flashcardSets.close()

                        # continues looping to create new flashcards 
                        while True:
                            # user enters flashcard term and definitions
                            userNewTerm = input('Enter the term of this flashcard\n>')
                            userNewDef = input('Input the definition of that term\n>')
                        
                            # opens flashcard term set and adds term 
                            with open(userChosenFlashcardSet + 'Term.txt','a') as newTermFile:
                                newTermFile.write(userNewTerm + '\n')
                                newTermFile.close()
                            # open flachard def set and adds definition
                            with open(userChosenFlashcardSet + 'Def.txt','a') as newDefFile:
                                newDefFile.write(userNewDef + '\n')
                                newDefFile.close()

                                # determines if you make another flashcard
                                continueEnteringFlashcards = input('\nDo you want to add another flashcard, y or n:\n>')
                                yOrN(continueEnteringFlashcards)
                                if continueEnteringFlashcards in YES:
                                    continue
                                elif continueEnteringFlashcards in NO:

                                    # determines if you make another flashcard set 
                                    continueFlashcard = input('\nDo you wish to continue making another flashcard set, y or n \n>')
                                    yOrN(continueFlashcard)
                                    if continueFlashcard in YES:
                                        # makes another flashcard set
                                        createFlashcard(userChosenSubject)

                                    elif continueFlashcard in NO:
                                        start()

                    # if input not in subject list then repeat loop till they enter a correct value 
                    else:
                        print("Please input a correct value")
                        readingSubject.close()
                        continue

def getFlashcards(userChosenSubject):
    with open(userChosenSubject + '.txt','r') as flashcardSets:
        # converts flashcardset file into a string by reading it 
        readFlashcardSets = flashcardSets.read()

        # converts flashcard set file into list 
        flashcardList = readFlashcardSets.split('\n')
        # removes last value, because its blank
        del flashcardList[-1]

        # asks user what flashcard set they would like to study
        userChosenFlashcardSet = input('\nPlease select your flashcard sets \nbelow you would like to study or go back:\n' + readFlashcardSets + ">")
        if userChosenFlashcardSet in goBack:
            flashcardSets.close()
            readSubject()
             
        elif userChosenFlashcardSet in flashcardList:
            flashcardSets.close()
            # coverts flashcard term file into a list
            with open(userChosenFlashcardSet + "Term.txt") as Terms:
                # makes term file as string
                termRead = Terms.read()
                # makes term a string (^) as list
                termsTotalList = termRead.split("\n") # turns string into list, by seperating each element by every entered line
                # removes empty line in list
                del termsTotalList[-1]
                # closes file
                Terms.close()
        
            # converts flashcard def file into a list
            with open(userChosenFlashcardSet + "Def.txt") as Def:
                 # makes def file as string
                defRead = Def.read()
                # make def a string (^) as list
                defsTotalList = defRead.split("\n") # turns string into list, by seperating each element by every entered line
                # removes empty line in list
                del defsTotalList[-1]
                # closes file
                Def.close()

            StudyChoice(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList)       
          
def StudyChoice(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    flashcardInfo = (userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList)
    while True:
        userStudyChoice = input("\nHow would you like to study:\n1. Flashcards \n2. Fill in the blanks \n3. Do a test \n4. Create notes, for this flashcard set in alphabetical order \n5. Match flashcards \n6. Multichoice \n7. Edit flashcards \n8. or go back\n>")
        
        # if user wants flashcards continue
        if userStudyChoice == "flashcards" or userStudyChoice == "Flashcards" or userStudyChoice == '1':
            StudyFlashcards(*flashcardInfo)

        # if user wants to fill in the blanks
        elif userStudyChoice == "Fill in the blanks" or userStudyChoice == "fill in the blanks" or userStudyChoice == "blanks" or userStudyChoice == '2':
            blanks(*flashcardInfo) 

        # if user wants to do a test 
        elif userStudyChoice == "Do a test" or userStudyChoice == "test" or userStudyChoice == "Test" or userStudyChoice == "do a test" or userStudyChoice == '3':
            test(*flashcardInfo)

        # if user wants to create notes 
        elif userStudyChoice == "Create notes" or userStudyChoice == "create notes" or userStudyChoice == "notes" or userStudyChoice == "Notes" or userStudyChoice == "Note" or userStudyChoice == "note" or userStudyChoice == '4':
            notes(*flashcardInfo)

        # if user wants to do a match up game 
        elif userStudyChoice == "match flashcards" or userStudyChoice == "Match flashcards" or userStudyChoice == "Match" or userStudyChoice == "match" or userStudyChoice == '5':
            matchFlashcards(*flashcardInfo)

        # if user wants to do multichoice 
        elif userStudyChoice == "multichoice" or userStudyChoice == "Multichoice" or userStudyChoice == "multi" or userStudyChoice == "Multi" or userStudyChoice == '6':
            multichoice(*flashcardInfo)

        # if user wants to go back
        elif userStudyChoice in goBack or userStudyChoice == '8':
            readSubject()

        # if user wants to edit or change their flashcards 
        elif userStudyChoice == 'edit' or userStudyChoice == 'Edit' or userStudyChoice == 'edit flashcards' or userStudyChoice == 'Edit flashcards' or userStudyChoice == '7':
            editFlashcards(*flashcardInfo)

        # makes user input correct value     
        else:
            print("please select a correct option")
            continue

def StudyFlashcards(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    flashcardInfo = (userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList)
    # counts position of flashcard, uses -1, as when starting while loop instantly ads a 1
    counter = -1
    # saves the index of the list flashcards you answer wrong
    wrongIndex = []

    # makes user input a valid answer
    while True:
        flashcardTermOrDef = input("\nWould you like to study by answering terms, or definitions or go back\n>")
        if flashcardTermOrDef in goBack:
            StudyChoice(*flashcardInfo)
        elif flashcardTermOrDef == "definitions" or flashcardTermOrDef == "Definitions" or flashcardTermOrDef == "Definition" or flashcardTermOrDef == "definition" or flashcardTermOrDef == "Def" or flashcardTermOrDef == "def" or flashcardTermOrDef == "Defs" or flashcardTermOrDef == "defs" or flashcardTermOrDef == "Terms" or flashcardTermOrDef == "terms" or flashcardTermOrDef == "term" or flashcardTermOrDef == "Term":
            break
        else:
            print("\nPlease input a correct value")
            continue
    # if user decides to answer with definitions, flashcardList1/2 will be equal to TermsList, DefList
    if flashcardTermOrDef == "definitions" or flashcardTermOrDef == "Definitions" or flashcardTermOrDef == "Definition"or flashcardTermOrDef == "definition" or flashcardTermOrDef == "Def" or flashcardTermOrDef == "def" or flashcardTermOrDef == "Defs" or flashcardTermOrDef == "defs":
        flashcardList1 = termsTotalList
        flashcardList2 = defsTotalList
    # if user decides to answer with definitions, flashcardList1/2 will be equal to DefList, TermList
    elif flashcardTermOrDef == "Terms" or flashcardTermOrDef == "Term" or flashcardTermOrDef == "terms" or flashcardTermOrDef == "term":
        flashcardList1 = defsTotalList
        flashcardList2 = termsTotalList

    while True:
        # counts the position of the flashcards
        counter = counter + 1

        # if all flashcards answered then move to flashcard decision
        if counter >= len(flashcardList1):
            flashcardDecision(wrongIndex, flashcardList1, flashcardList2, *flashcardInfo)
        
        # showing flashcard section of code
        print(flashcardList1[counter])
        input("\nPress enter to reveal definition \n>")
        print(flashcardList2[counter])
        rightOrWrong = input("\nDid you get the flashcard right, y or n \n>")

        # makes sure user answer is valid
        yOrN(rightOrWrong)

        # if user answered flashcard correctly then don't add counter num (index of list) to wrongIndex
        if rightOrWrong in YES:
            continue
        # if user answered flashcard incorrectly then adds counter num (index of list) to wrongIndex
        else:
            wrongIndex = wrongIndex + [counter]
            continue

def wrongFlashcard(wrongIndex, flashcardList1, flashcardList2, termsTotalList, defsTotalList, userChosenSubject, userChosenFlashcardSet):
    flashcardInfo = (termsTotalList, defsTotalList, userChosenSubject, userChosenFlashcardSet)
    # keeps track of the position of the list, of for wrongIndex
    counter2 = -1
    # keeps track of how many times a element has been removed from wrong index 
    counter3 = 0

    print("\nThese are the flashcards you got wrong, \ntry to remember them to the best of your ability")

    while True:
        # keeps track of how many times loop had been repeated 
        counter2 = counter2 + 1

        # if all flashcards answered correctly then go back to flashcardDecision
        if wrongIndex == []:
            print("Good job, you remembered all the flashcards")
            flashcardDecision(wrongIndex, flashcardList1, flashcardList2, *flashcardInfo)

        # once user gone through all flashcards, repeats ones answered incorrectly and sets counters back to beginning 
        if counter2 + counter3 >= len(wrongIndex):
            counter2 = -1
            counter3 = 0
            continue
        
        # showing flashcard section of code 
        print(flashcardList1[(wrongIndex[counter2 + counter3])])
        input("\nPress enter to reveal definition \n>")
        print(flashcardList2[(wrongIndex[counter2 + counter3])])


        rightOrWrong = input("\nDid you get the flashcard right, y or n \n>")
        # makes sure user input is valid
        yOrN(rightOrWrong)
        # if user answered flashcard correctly removes flashcard from the deck (wrongIndex) so to speak
        if rightOrWrong in YES:
            # deletes flashcard position from wrongIndex
            del wrongIndex[(counter2 + counter3)]
            counter3 = counter3-1
            continue
        # if user did not get flashcard right, keep it and continue to loop
        else:
            continue

def flashcardDecision(wrongIndex, flashcardList1, flashcardList2, termsTotalList, defsTotalList, userChosenSubject, userChosenFlashcardSet):
    flashcardInfo = (termsTotalList, defsTotalList, userChosenSubject, userChosenFlashcardSet)
    while True:
        options = input("\nWould you like to: \n1. continue doing flashcards, \n2. redo this flashcard set or \n3. go back to study options \n>")
        
        # if user wishes to continue 
        if options == "continue" or options == "Continue" or options == "Continue flashcards" or options == "continue flascards" or options == "flashcards" or options == "Flashcards" or options == '1' or options == '1.':
            if wrongIndex == []:
                StudyFlashcards(*flashcardInfo)
            else:
                wrongFlashcard(wrongIndex, flashcardList1, flashcardList2, *flashcardInfo)
        
        # if user wants to redo flashcards 
        elif options == "Redo" or options == "redo" or options == '2' or options == '2.':
            StudyFlashcards(*flashcardInfo)
        
        # if user wants to go back 
        elif options in goBack or options == '3' or options == '3.':
            StudyChoice(*flashcardInfo)

# creats notes, ordered a to z
def notes(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    flashcardInfo = (termsTotalList, defsTotalList, userChosenSubject, userChosenFlashcardSet)
    counter = -1
    position = []
    
    # sorts the terms into alphabetical order 
    sortedTermList = []
    sortedTermList = sortedTermList + sorted(termsTotalList)

    # finds position to original list 
    counter = 0
    position = []
    while counter < len(termsTotalList):
        position = position + [termsTotalList.index(sortedTermList[counter])]
        counter = counter + 1

    counter = 0
    # wrights notes into text file 
    with open(str(userChosenSubject) + ' ' + str(userChosenFlashcardSet) + ' Note.txt','a') as userNotes:
        while counter < len(termsTotalList):
            userNotes.write(sortedTermList[counter] + "\n")
            userNotes.write(defsTotalList[(position[counter])] + "\n\n")
            counter = counter + 1
    
    print("\nYour notes have been created \nthe file name is: \n" + str(userChosenSubject) + ' ' + str(userChosenFlashcardSet) + ' Note.txt\n')
    userNotes.close()
    StudyChoice(*flashcardInfo)

def matchFlashcards(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    flashcardInfo = (userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList)
    # list of alphabete capitals, and lowercase 
    L = list(ascii_lowercase) + [letter1 + letter2 + letter3 for letter1 in ascii_lowercase for letter2 in ascii_lowercase for letter3 in ascii_lowercase]
    U = list(ascii_uppercase) + [letter1 + letter2 + letter3 for letter1 in ascii_uppercase for letter2 in ascii_uppercase for letter3 in ascii_uppercase]
    
    # determines if enough flashcards are present
    while True:
        if len(termsTotalList) < 5:
            print("You need at least five flashcards to use this function\n")
            StudyChoice(*flashcardInfo)
        else:
            break

    # determines how many flashcards user would like to match, 
    while True:
        numInput = input("How many flashcards would you like to match\n>")
        # checks if input is a number or word, converts word to number if a number word 
        num = checkIsDigit(numInput)
        # makes sure user doesn't enter five flashcards
        if int(num) < 5:
            print("Less then five flashcards is too easy, pick something higher")
            continue

        while True:
            # if enough flashcards continue 
            if num <= len(termsTotalList):
                break
            # if not enough flashcards are available for number, loops back 
            else:
                numInput = input("Please enter a number within your number of flashcards \nYou have " + str(len(termsTotalList)) + " flashcards \n>")
                # checks if input is a number or word, converts word to number if a number word 
                num = checkIsDigit(numInput)

        # shuffles list 1
        randomShuffle1 = random.sample(termsTotalList,int(num))
        # save shuffled order to shuffledList1
        shuffledList1 = []
        shuffledList1 = shuffledList1 + randomShuffle1

        indexCounter = []
        # used to give index order of new list in comparison to original order of list1
        counter = -1 
        while True:
            counter = counter + 1
            if counter >= int(num):
                break
            indexCounter = indexCounter + [termsTotalList.index(randomShuffle1[counter])]

        # make selectedList2 correspond with shuffled list1
        selectedList2 = []
        counter = -1
        while True:
            counter = counter + 1
            if counter>= int(num):
                break
            selectedList2 = selectedList2 + [defsTotalList[indexCounter[counter]]]

        # shuffles the order of list2 
        randomShuffle2 = random.sample(selectedList2,int(num))
        # saves shuffle order 
        shuffledList2 = []
        shuffledList2 = shuffledList2 + randomShuffle2

        # used to give index order of new list in comparison to original order of list2
        indexCounter2 = []
        counter = -1
        while True:
            counter = counter + 1
            if counter >= int(num):
                break
            indexCounter2 = indexCounter2 + [defsTotalList.index(shuffledList2[counter])]

        # creates dictionary of terms to defs being used
        answerKey = {}
        counter = -1 
        while True:
            counter = counter + 1
            if counter >= int(num):
                break
            # adds term and def to dictionary
            answerKey.update({shuffledList1[counter]: selectedList2[counter]})

        # creates dictionary of terms to defs being used
        answerKeyChecker = {}
        counter = -1
        wrong = 0
        correct = 0
        while True:
            counter = counter + 1
            if counter >= int(num):
                break
            # adds term and def to dictionary
            answerKeyChecker.update({(shuffledList1[counter]): (selectedList2[counter])})

        # creates list of left column letters
        counter = -1
        listLeftColumnLetters = []
        while True:
            counter = counter + 1
            if counter >= int(num):
                break
            listLeftColumnLetters = listLeftColumnLetters + [L[counter]]
            continue

        # creates list of right column letters
        counter = -1
        listRightColumnLetters = []
        while True:
            counter = counter + 1
            if counter >= int(num):
                break
            listRightColumnLetters = listRightColumnLetters + [U[counter]]

        # prints the left and right columns to match up
        matchOptionInfo = (answerKeyChecker, listLeftColumnLetters, shuffledList1, listRightColumnLetters, shuffledList2)
        printMatchOptions(*matchOptionInfo)

        # determines how many times have looped
        countStartDone = 0

        # if matched all flashcards
        userInputTotalList = []
        while True:
            if correct >= int(num):
                print("You have matched all flashcards\n")
                end_time = time.time()
                time_lapsed = end_time - start_time
                break

            # if first time running this loop, print instructions
            if countStartDone < 1:
                print("Match up the terms on left, to definitions on right, \nEnter using given variable, example input left column 'a' input right column'C' \nA timer will start once you have entered the left column, to see how fast you are\n")

            # users input for left collumn
            userInputLeft = input("input left column\nor go back \n>")
            if userInputLeft in goBack:
                StudyChoice(*flashcardInfo)

            # starts stopwatch if first time running
            if countStartDone < 1:
                start_time = time.time()
    
            # how many times this person has run this loop
            countStartDone = countStartDone + 1
            # user input for right column
            userInputRight = input("input right column\n>")

             # adds user total answer into a list
            userInputTotalList = []
            counter = -1
            while True:
                counter = counter + 1
                # if input is not in column, then makes user input correct value
                if counter >= int(num - correct):
                    printMatchOptions(*matchOptionInfo)
                    userInputLeft = input("Please input a correct value for left column\n>")
                    counter = -1
                    continue

                # finds user input for left column
                elif str(userInputLeft) == str(listLeftColumnLetters[counter]):
                    userInputTotalList = userInputTotalList + [shuffledList1[counter]]
                    break
                continue

            # finds input for right column   
            counter = -1
            while True:
                counter = counter + 1 
                # if input is not in column, then makes user input correct value
                if counter >= int(num - correct):
                    printMatchOptions(*matchOptionInfo)                    
                    userInputRight = input("Please input a correct value for right column\n>")
                    counter = -1

                # finds input for right column      
                elif userInputRight == listRightColumnLetters[counter]:
                    userInputTotalList = userInputTotalList + [shuffledList2[counter]]
                    break

            # if user total answer is correct
            if answerKeyChecker.get(userInputTotalList[0]) == userInputTotalList[1]:
                # removes flashcard from answer key 
                del answerKeyChecker[userInputTotalList[0]]
                # removes term from list1
                shuffledList1.remove(userInputTotalList[0])
                # removes corresponding letter from list1
                listLeftColumnLetters.remove(userInputLeft)
                # removes def from list2
                shuffledList2.remove(userInputTotalList[1])
                # removes corresponding letter from list2
                listRightColumnLetters.remove(userInputRight)
                print("CORRECT\n")
                printMatchOptions(*matchOptionInfo)
                correct = correct + 1

            # determines if already answered flashcard
            elif  answerKey.get(userInputTotalList[0]) == userInputTotalList[1]:
                print("You have already matched this set\n")
                printMatchOptions(*matchOptionInfo)

            # determines if answer is wrong
            else:
                print("WRONG\n")
                wrong = wrong + 1
                printMatchOptions(*matchOptionInfo)

        # prints time taken
        timeConvert(time_lapsed)
        # prints how many answers you got wrong 
        print("you got " + str(wrong) + " wrong")
        StudyChoice(*flashcardInfo)    

# actual fill in the blanks 
def blanks(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    # used information to go back to study options 
    flashcardInfo = (userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList)
    
    difficulty = input("\nHow difficult would you like it to be \nEasy \nMedium \nHard \n>")
    while True:
        # if user wants to do easy difficulty 
        if difficulty == "easy" or difficulty == "Easy":
            mode = 20
            break

        # if user wants to do medium difficulty 
        elif difficulty == "medium" or difficulty == "Medium":
            mode = 40
            break

        # if user wants to do hard difficulty 
        elif difficulty == "hard" or "Hard":
            mode = 60
            break

        # if user hasn't put in a correct value 
        else:
            difficulty = input("Please input a correct value \n>")
            continue

    # determine amount looped, uses number to determine what element in list, user is on
    counterDef = -1

    # determine how much user got right and wrong
    correctTotal = 0
    wrong = 0

    while True:
        correct = 0
        # used to determine what definition user is on 
        counterDef = counterDef + 1

        # only if counterDef is equal to the number of definitions
        if counterDef >= len(defsTotalList):
            print("You have completed all flashcards")
            StudyChoice(*flashcardInfo)

        # used to break up definition user is on, into individual readable words 
        defElement = defsTotalList[counterDef]
        defSplit = defElement.split(" ")
        defListOriginal = []
        defListOriginal = defListOriginal + defSplit

        # determines amount to replace 
        amount = math.ceil(mode/100*len(defListOriginal))

        # samples flashcards to replace
        sampleListDefs = [] 
        sampleListDefs = random.sample(defListOriginal, amount)
        editListDef = []
        editListDef = editListDef + sampleListDefs

        # finds correct position to original list and put them in order 
        position = []
        counter = -1
        while True:
            counter = counter + 1
            if counter >= amount:
                break
            position = position + [defListOriginal.index(sampleListDefs[counter])]
        position.sort()

        # gives number list, that will be used towards answerKey, compare userNum to userAnswer
        number = -1
        numberListsAnswer = []
        while True:
            number = number + 1
            if number >= amount:
                break
            numberListsAnswer = numberListsAnswer + [number]

        # makes number list ready for printing
        numberDisplay = []
        counter = -1
        while True:
            counter = counter + 1
            if len(numberDisplay) == len(numberListsAnswer):
                break
            numberDisplay = numberDisplay + ["____"+str(numberListsAnswer[counter]) + "____"]

        # sorts the random sampled list into order 
        sortedListDefs = []
        counter = -1
        while True:
            counter = counter + 1
            if counter >= amount:
                break
            sortedListDefs = sortedListDefs + [defListOriginal[position[counter]]] 

        while True:
            # determines if all answer are correct for this definition 
            if correct >= amount:
                break

            # replaces variables
            defList = defListOriginal
            counter = -1
            while True:
                counter = counter + 1
                if counter >= amount - correct:
                    break
                defList = [w.replace(sortedListDefs[counter], numberDisplay[counter]) for w in defList]

            # removes commars and any non important variables from list, to have user answer checked against 
            sortedListDefs = checkNotImportant(sortedListDefs)

            # makes answer key to check user input against
            answerKeyChecker = {}
            counter = -1
            while True:
                counter = counter + 1
                if counter >= amount - correct:
                    break
                # adds number to def in dictionary 
                answerKeyChecker.update({numberListsAnswer[counter]: sortedListDefs[counter]})   

            if correct < 1:
                # used to check against if user already answered
                answerKey = {}
                counter = -1
                while True:
                    counter = counter + 1
                    if counter >= amount:
                        break
                    # adds number to definition in dictionary 
                    answerKey.update({numberListsAnswer[counter]: sortedListDefs[counter]})

            # prints term to fill in 
            print("\nYour Term is: \n" + str(termsTotalList[counterDef]) + '\n')
            
            # prints def list, with replaced words 
            print(' '.join(str(x) for x in defList))

            # if user wants to go back 
            numInput = input("Input the number you want to answer or go back \n>")
            if numInput in goBack:
                StudyChoice(*flashcardInfo)

            # checks if input is a number or word, converts word to number if a number word 
            nums = checkIsDigit(numInput)
            userInputAnswer = input("\nInput the answer of that number \n>")

            # removes what is within brackets in a string, removes notImportant information, converts string to lowercase
            userInputAnswer = checkNotImportant(userInputAnswer)

            # adds user chosen number, and answer to userTotalAnswer
            userTotalAnswer = []
            userTotalAnswer = userTotalAnswer + [int(nums)]
            userTotalAnswer = userTotalAnswer + [userInputAnswer]
            
            
            # if user answer correctly continues 
            if userTotalAnswer[1] in answerKeyChecker.get(int(userTotalAnswer[0])):
                print("CORRECT")
                # deletes question from list
                del answerKeyChecker[userTotalAnswer[0]]
                # remove question number to display fro list 
                del numberDisplay[numberListsAnswer.index(int(userTotalAnswer[0]))]
                # removes question number from list 
                numberListsAnswer.remove(int(userTotalAnswer[0]))
                # removes answer from list
                sortedListDefs.remove(userTotalAnswer[1])
                # adds a correct score
                correct = correct + 1
                # used to find total correct score 
                correctTotal = correctTotal + 1
            
            # if user repeated a number 
            elif userTotalAnswer[1] in answerKey.get(int(userTotalAnswer[0])):
                print("You have already completed this one")

            # if user has entered wrong answer 
            else:
                print("WRONG \nTry again")
                wrong = wrong+1
            continue
        continue

def multichoice(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    # flashcard info 
    flashcardInfo = (userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList)

    # makes sure user has enough flashcards to be able to use this function
    if len(termsTotalList) < 4:
        print("You do not have enough flashcards for this mod, \nyou need at least four, you only have " + str(len(termsTotalList)) + " flashcards")
        StudyChoice(*flashcardInfo)


    # adds flashcards terms to termChoice, in which they can be edited, and removed 
    termChoice = []
    termChoice = termChoice + termsTotalList

    # used as list for lowercase letters up to three digits "abc"
    L = list(ascii_lowercase) + [letter1+letter2+letter3 for letter1 in ascii_lowercase for letter2 in ascii_lowercase for letter3 in ascii_lowercase]

    # total amount of correct answers
    correct = 0

    # total value of incorrect answers 
    wrong = 0
    while True:
        # if completed all flashcards, ends 
        if correct == len(termsTotalList):
            print("You have matched all flashcards")
            # displays amount right and wrong
            print("You got " + str(correct) + " correct, and \n you got " + str(wrong) + " wrong")
            # little message for how many user got right and wrong 
            if correct - wrong <= 0:
                print("Better luck next time")
            elif wrong >= 0:
                print("EXCELENT WORK")
            elif correct - wrong > 0:
                print("Good job")
            StudyChoice(*flashcardInfo)

        # picks a random term, for user to answer
        term = random.sample(termChoice, 1)
        # finds the corresponding term to the answer 
        Def = defsTotalList[termsTotalList.index(term[0])]

        # makes a list of all definitions, excluding the correct one
        sampleOptions = []
        sampleOptions = sampleOptions + defsTotalList
        # removes correct definition from the list 
        sampleOptions.remove(Def)
        # randomly picks three definitions to add to the multichoice that is not the correct definition
        randomSample = random.sample(sampleOptions,3)

        # adds randomly incorrect choices to the list and correct choice
        displayList = []
        displayList = displayList + randomSample
        displayList = displayList + [Def]
        # shuffles the choices, in how they are displayed 
        random.shuffle(displayList)

        # creates a list of letters, length of 4
        listLetters = []
        counter = -1
        while True:
            counter = counter+1
            if counter >= 4:
                break
            listLetters = listLetters + [L[counter]]

        # used to display choices to answer term, with corresponding letters 
        counter = -1
        while True:
            counter = counter + 1
            if counter == 4:
                break
            print(listLetters[counter]+".   "+displayList[counter])

        # the options user can pick, with corresponding definitions
        options = {}
        counter = -1 
        while True:
            counter = counter + 1
            # adds the amount of the options displayed, which are four 
            if counter == 4:
                break 
            # adds corresponding letters to definition in dictionary 
            options.update({listLetters[counter]: displayList[counter]})

        # explains instructions for the first time 
        print("Your term is: " + str(term[0]))
        if wrong or correct <= 0:
            print("To enter your definition, answer by inputing the letter, like 'a'")

        # users choice of definitions
        userInput = input("Enter the definition that matches this term, or go back \n>")

        if userInput in goBack:
            StudyChoice(*flashcardInfo)

        while True:
            # if user has inputed a correct value 
            if userInput in listLetters:

                # if users input is correct
                if options.get(userInput) == Def:
                    print("CORRECT\n")
                    # removes the term to be answered from list, so it is not repeated
                    termChoice.remove(term[0])
                    # adds one correct value
                    correct = correct + 1
                    break

                # if user input is wrong
                else:
                    print("WRONG\n")
                    # adds a wrong value to score 
                    wrong = wrong + 1
                    break

            # if user has not inputed a correct value 
            else:
                # used to display choices to answer term, with corresponding letters 
                counter = -1
                while True:
                    counter = counter + 1
                    if counter == 4:
                        break
                    print(listLetters[counter] + ".   " + displayList[counter])
                
                userInput = input("please enter a correct value ")

def test(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    # flashcard info 
    flashcardInfo = (userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList) 
    # time limit 
    print("Input the time limit, in hours, minutes, seconds")
    # converted to seconds 
    hours = int(input("input hours: ")) * 3600
    # converted to seconds 
    minutes = int(input("input minutes: ")) * 60
    second = int(input("input seconds: "))


    timeDuration = hours + minutes + second
    # used to time length of time per second
    timeStart = time.time()

    # used for testing terms and defs
    terms = []
    defs = []

    # amount of flashcards 
    amount = input('\nInput the amount of flashcards you would like to do, \ntake into consideration the amount of time you set yourself \n>')
    amount = checkIsDigit(amount)
    # if user gives an incorrect value, something not a number 
    while int(amount) < 0:
        amount = input('\nPlease input a correct value\n')
        amount = checkIsDigit(amount)
    
    # if user gives a greater number, then number of flashcards 
    while int(amount) > len(termsTotalList):
        amount = input('\nYou have given a number that is greater then \nthe amount of flashcards you have, you have ' + str(len(termsTotalList)) + '\nflashcards, input a number equal too or below this amount \n>')
        amount = checkIsDigit(amount)

    # takes amount of flashcards you have given
    terms = terms + random.sample(termsTotalList, int(amount))

    # finds index of shuffled list to original list
    Index = []
    counter = -1 
    while True: 
        counter = counter + 1
        if counter >= int(amount):
            break
        Index = Index + [termsTotalList.index(str(terms[counter]))]

    # gives the correct definition corresponding to the position of shuffled terms
    counter = 0
    while counter < int(amount):
        defs = defs + [defsTotalList[Index[counter]]]
        counter = counter + 1

    # make definitions into answers not containing not important information 
    defs = checkNotImportant(defs)

    # makes answer key for terms and definitions, in correct order, term 1 is def 1, even when shuffled
    flashcardList = {}
    counter = -1 
    while True:
        counter = counter + 1
        if counter >= int(amount):
            break 
        # adds term to definition to dictionary 
        flashcardList.update({terms[counter]:defs[counter]})

    # variables to be used when answering
    correct = 0             # used to determine how many correct answers user entered
    wrong = 0               # used to determine how many incorrect answers user entered
    wrongFlashcards = []    # records position (index) of which answers user got wrong
    userAnswerWrong = []    # records the user incorrect answer
    skip = []               # used to determing position of skiped answers

    skipCounter = 0         # number of times term has been removed without resetting
    counter = -1            # counter for first questions, not skiped 
    counter2 = -1           # counter for skiped questions 

    # continues to allow user to answer if not gone over time limit they entered 
    while time.time() < timeStart + timeDuration:
        counter = counter  + 1
        # if answered all questions moves on to the ones user skiped 
        if counter == len(flashcardList):
            # if user did not skip any questions do not continue 
            if skip == []:
                break
            print("\nThese are the questions you skiped \n")
            counter2 = -1
            # while there are still positions of flashcards of ones skipped, continue
            while skip != []: 
                counter2 = counter2 + 1
                # resets the counters back to original once user has gone through all flashcards 
                if skipCounter + counter2 == len(skip):
                    counter2 = 0
                    skipCounter = 0
                print("Your term is: " + list(flashcardList)[skip[counter2 + skipCounter]])
                answer = input("Input your answer for this definition \n>")
                answer = checkNotImportant(answer) # removes all not important information from users answer

                if answer in goBack:
                    StudyChoice(*flashcardInfo)
                # if user answer is correct to the definition continue below 
                elif flashcardList.get(list(flashcardList)[skip[counter2 + skipCounter]]) == answer:
                    correct = correct + 1 
                    # removes position of flashcard, so it is not repeated again 
                    del skip[counter2 + skipCounter] 
                    # removes number to allow program to know that there is one less variable in skip
                    skipCounter = skipCounter - 1
                
                # if user skiped continue below
                elif answer == 'skip':
                    continue
                # if user answered wrong continue below 
                else:
                    wrong = wrong + 1
                    # adds position two list of incorrect answer 
                    wrongFlashcards = wrongFlashcards + [skip[counter2 + skipCounter]]
                    # adds users incorrect answer to be displayed latter 
                    userAnswerWrong = userAnswerWrong + [answer]
                    # removes position of flashcard, so it is not repeated again 
                    del skip[counter2 + skipCounter]
                    # removes number to allow program to know that there is one less variable in skip
                    skipCounter = skipCounter - 1
            # onces answered every question, breaks out of loop 
            break            

        print("Your term is: " + str(list(flashcardList)[counter]))
        if counter <= 0:
            answer = input("Input your answer for this definition, \nor skip the question, if you have time you can come back to this question \nor go back \n>")
        else:
            answer = input("Input your answer for this definition, skip, or go back \n>")
        answer = checkNotImportant(answer) # removes all not important information from users answer

        # if user decides to go back (quit)
        if answer in goBack:
            StudyChoice(*flashcardInfo)
        # if user answer is correct continue below 
        elif flashcardList.get(list(flashcardList)[counter]) == answer:
            # adds one correct
            correct = correct + 1
        # if user skiped, adds position of skiped flashcard to skip
        elif answer == 'skip':
            skip = skip + [counter]
        # if user answered wrong continue below 
        else:
            # adds wrong
            wrong = wrong + 1
            # adds position of incorrect answer 
            wrongFlashcards = wrongFlashcards + [counter]
            # adds user incorrect answer to be displayed later 
            userAnswerWrong = userAnswerWrong + [answer]

    # if user ran out of time display below 
    if counter != len(flashcardList) or skip != []:
        print("Times up ")
    # if user did not run out of time, display below 
    else:
        print("You have answered all questions, well done")

    # calculates percentage of users score
    percentage = int(correct / len(flashcardList) * 100)
    print("You got " + str(correct) + " right, and " + str(wrong) + " wrong, thats " + str(percentage) + "%")

    # grade rating 
    if percentage > 70:
        print("EXCELENT \n")
    elif 50 < percentage > 70:
        print("Good job \n")
    else:
        print("Better luck next time \n")

    # if user got answers wrong displays them below
    if wrongFlashcards != []:
        print("These were the questions you got wrong \n")
        # variables of original score and new score
        newWrong = 0
        newWrong = newWrong + wrong
        newCorrect = 0
        newCorrect = newCorrect + correct
        counter = -1
        while True:
            counter = counter + 1
            # if gone through all incorrect flashcards 
            if counter >= len(wrongFlashcards):
                break
            # prints term
            print("The term was: " + str(list(flashcardList)[wrongFlashcards[counter]]))
            # prints user answer 
            print("Your answer was: \n" + str(userAnswerWrong[counter]))
            # prints correct answer 
            print("The correct answer was: \n" + str(flashcardList.get(str(list(flashcardList)[wrongFlashcards[counter]]))) + '\n')
            # allows user to say if they should have got this flashcard right or wrong, as due to wording, grammar, etc
            changeAnswer = input("did you get this right, y or n \n>")
            yOrN(changeAnswer)
            # if user got flashcard right update score 
            if changeAnswer in YES:
                newWrong = newWrong -1
                newCorrect = newCorrect + 1
            print('\n')

        # if score is the same
        if newWrong == wrong and newCorrect == correct: 
            print("\nYour score is still " + str(percentage) + '% you got ' + str(correct) + ' right, and ' + str(wrong) + ' wrong')
        # if score is different
        else:
            percentage = int(newCorrect / len(flashcardList) * 100)
            print("\nYour new score is " + str(percentage) + '% you got ' + str(newCorrect) + ' right, and ' + str(newWrong) + ' wrong')
        # grade rating
        if percentage > 70:
            print("EXCELENT \n")
        elif 50 < percentage > 70:
            print("Good job \n")
        else:
            print("Better luck next time \n")
    StudyChoice(*flashcardInfo)

def editFlashcards(userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList):
    # flashcard information 
    flashcardInfo = (userChosenSubject, userChosenFlashcardSet, termsTotalList, defsTotalList) 

    counter = 0
    while counter < len(termsTotalList):
        # prints terms and definiton
        print('\nTerm: ' + termsTotalList[counter])
        print('Definition: ' + defsTotalList[counter] + '\n')
        # if user wants to edit flashcard continue below 
        decision = input('Do you want to edit this flashcard, y or n, or you can go back \n>')
        if decision in goBack:
            StudyChoice(*flashcardInfo)
        # makes sure user input a correct value 
        yOrN(decision)
        if decision in YES:
            newTerm = input("\nWhat would you like the new term to be, \nenter nothing if you do not want to change the term, \nor go back \n>")
            if newTerm in goBack:
                StudyChoice(*flashcardInfo)
            if newTerm != '':
                # finds index location of editing term
                IndexTerm = termsTotalList.index(termsTotalList[counter])
                # replaces the term to the new term, using index as positioning
                termsTotalList = termsTotalList[:IndexTerm] + [str(newTerm)] + termsTotalList[IndexTerm+1:]
            newDef = input("\nWhat would you like the new definition to be, \nenter nothing if you do not want to change the definition, \nor go back \n>")
            if newDef in goBack:
                StudyChoice(*flashcardInfo)
            if newDef != '':
                # finds index location of editing definition
                IndexDefs = defsTotalList.index(defsTotalList[counter])
                # replaces the definition to the new definition, using index as positioning
                defsTotalList = defsTotalList[:IndexDefs] + [str(newDef)] + defsTotalList[IndexDefs+1:]
        counter = counter + 1

    # prints flashcards 
    counter = 0
    while counter < len(termsTotalList):
        print('term: ' + termsTotalList[counter] + '        ' + 'definition: ' + defsTotalList[counter] + '\n')
        counter = counter + 1
    satisfied = input('Is list of terms and definitions to your satisfaction, y or n \n>')
    yOrN(satisfied)

    # if user is not satified with flashcards, starts function again
    if satisfied in NO:
        toStartOfFunction(editFlashcards,flashcardInfo)

    # edits flashcard term set
    with open(userChosenFlashcardSet + 'Term.txt','w') as newTermFile:
        for termWords in termsTotalList:
            newTermFile.write(termWords + '\n')
        newTermFile.close()

    # edits flashcard def set
    with open(userChosenFlashcardSet + 'Def.txt','w') as newDefFile:
        for defWords in defsTotalList:
            newDefFile.write(defWords + '\n')
        newDefFile.close()

    # goes back to study choices 
    print('\nYour flashcards have been changed\n')

    # goes back to study options
    StudyChoice(*flashcardInfo)

# starting function of program      
start()                                