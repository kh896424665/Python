import random, string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words.
    Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish."""

    print("Loading word list from file...")

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord,lettersGuessed):
    secretWord = secretWord.lower()
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getguessedWord(secretWord, lettersGuessed):
    secretWord = secretWord.lower()
    blanks = "_" * len(secretWord)
    blanks_list = list(blanks)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            blanks_list[i] = secretWord[i]
    return " ".join(blanks_list)


def getAvailableLetters(lettersGuessed):
    availableLetters = " "
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            availableLetters += i
    return availableLetters


def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {0} letters long.".format(len(secretWord)))
    num = 8
    lettersGuessed = []

    while num>0:
        print("*************")
        print("You have {0} guesses left.".format(num))
        print("Available letters:",getAvailableLetters(lettersGuessed))
        guess = str(input("Please guess a letter:"))
        guessInLowerCase = guess.lower()
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:",getguessedWord(secretWord, lettersGuessed))
        elif guessInLowerCase in secretWord:
            lettersGuessed.append(guessInLowerCase)
            print("Good guess:",getguessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord,lettersGuessed):
                print("*************")
                print("Congratulations, you won!")
                num = -1    #成功，结束
        else:
            lettersGuessed.append(guessInLowerCase)
            print("Oops! That letter is not in my word:",getguessedWord(secretWord, lettersGuessed))
            num = num-1

    if num == 0:     #次数用光，game over
        print("*************")
        print("Sorry, you ran out of guesses. The word was fit")

wordlist=loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
