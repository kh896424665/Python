# Hangman is a game for two people usually played with paper and pencil.
# One player thinks of a word, and then draws a blank on the page for
# each letter in the word. Then the second player tries
# to guess letters that might be in the word (猜字游戏)
import random

HangManPics = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',

'''
  |   |
  O   |
 /|   |
      |
      |
=========''',

'''
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',

'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',

'''
  +----+
  |    |
 [O    |
 /|\   |
 / \   |
       |
=========''',

'''
  +----+
  |    |
 [O]   |
 /|\   |
 / \   |
       |
=========''']

animal_words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion
lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon
python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake 
spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'''

color_words = '''red orange yellow green blue indigo violet white black brown'''

shape_words = '''square triangle rectangle circle ellipse rhombus trapezoid chevron
pentagon hexagon septagon octagon'''

fruit_words = '''apple orange lemon lime pear watermelon grape grapefruit cherry banana
cantaloupe mango strawberry tomato'''

# 利用以上的字符串，生成words字典
# 字典的形式如 {key1:value1,key2:value2,....,keyn:valuen}
# 字典的键是每种类别的名称，每个键的值是该类别所有种类构成的列表
# 请补充完成words字典的定义
words = {'Colors':color_words.split(),'Shapes':shape_words.split(),'Fruits':fruit_words.split(),'Animals':animal_words.split()}


# this function take the words dictionary, and randomly choose a type (such as the color)
# then randomly choose a word in the choosen type (such as yellow),
# which is used as the secretWord
# the function returns the secretWord and its type
def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0,len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex],wordKey]


# write a function called displayBoard
# the function displays the board and the Missed letters
# the function takes the following four parameters

"""
1) HangManPics - A list of multi-line strings that will display the board as ASCII art.
2) missedLetters - A string of the letters the player has guessed that are not in the secret word.
3) correctLetters - A string of the letters the player has guessed that are in the secret word
4) secretword - A string of the secret word that the player is trying to guess.
"""


# all the letters in the secretWord are displayed as '_'
# if the letter in secretWord is presented in correctLetters, then '_' is replaced by the correct letter
def displayBoard(HangManPics, missedLetters, correctLetters, secretWord):
    # print the current state of HandManPics，then print a blank line
    print(HangManPics[len(missedLetters)])
    print()
    # print the prompt message "Missed letters:" and all letters in missedLetters
    # in order to make the output clearly, we add a blank character after each letter
    # then print a blank line
    print("Missed letters:" + " ".join(list(missedLetters)))
    print()
    # create a copy of secret word, called blanks, and all letters in blanks are '_'
    # use a for loop to change blanks
    # in order to replace the '_' in blanks with the correct letter in secretWord
    # namely, if one letter in secretWord is in correctLetters, then replace
    blanks = '_' * len(secretWord)
    blanks_list = list(blanks)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks_list[i] = secretWord[i]
            # print the prompt message "Correct letters:" and all letters in blanks
    # in order to make the output clearly, we add a blank character after each letter
    # then print a blank line
    print("Correct letters:" + " ".join(blanks_list))
    print()


# write a function called getGuess, which takes a parameter alreadyGuessed
# the function asks the user to input a single letter
"""
if the user doesn't input single letter,
or input already guessed letter,
or input letters not in  'abcdefghijklmnopqrstuvwxyz',
the function prints hint message and requires
the user to input again unitl the user inputs a 
satisfied single letter.
"""


# your code is here
def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter:")
        user_input = input()
        if len(user_input) >= 2:
            print("Please enter a single letter.")
        elif user_input in alreadyGuessed:
            print("You have already guessed that letter.Choose again.")
        elif user_input < "a" or user_input > "z":
            print("Please enter a LETTER.")
        else:
            return user_input


# write a function called playAgain, which return a boolean value True or False
# the function takes the user's input
# if the user input yes, then the function return True, else return False
def playAgain():
    print('Do you want to play again?(yes or no)')
    # write a single line code to finish this function
    return input().lower() =="yes"


# the body of this game
print('H A N G M A N')

# the initial state
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretKey)
    # use the function displayBoard to display the board
    displayBoard(HangManPics, missedLetters, correctLetters, secretWord)
    # use the functin getGuess to get user's guess
    # and set the user's guess in a variable named guess
    guess = getGuess(missedLetters + correctLetters)
    # if the guessed letter in secretWord
    if guess in secretWord:
        correctLetters += guess
        foundAllLetters = True
        # use the for loop to test whether all letters in secretWord are in correctLetters,
        # if not, set foundAllLetters to False
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        # if foundAllters is True
        # then print the sentence like the one in the sample output
        # and set gameIsDone to True
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        # change missedLetters
        missedLetters += guess
        if len(missedLetters) == len(HangManPics) - 1:
            # use the function displayBoard to display the board
            displayBoard(HangManPics, missedLetters, correctLetters, secretWord)
            # print the sentence like the one in the sample output
            # and set gameIsDone to True
            print("You have run out of guesses!")
            print("After %d missed guessed and %d correct guesses,the word was '%s'" % (
            len(missedLetters), len(correctLetters), secretWord))
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            # set the initial state
            missedLetters = ''
            correctLetters = ''
            secretWord, secretKey = getRandomWord(words)
            gameIsDone = False

        else:
            break
