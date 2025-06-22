from english_words import get_english_words_set
import random

GUESSES_PER_GAME: int = 6

RED     =   "\033[1;31m"
YELLOW  =   "\033[1;33m"
GREEN   =   "\033[1;32m"
OFF     =   "\033[0;0m "

def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

def createListOfNLetterWords(n) -> list:
    if n == 5:
        with open("guesses.txt", "r") as guesses:
            validGuesses = [rchop(line, "\n") for line in guesses]
        with open("answers.txt", "r") as answers:
            validAnswers = [rchop(line, "\n") for line in answers]

        return validGuesses, validAnswers

    web2lowerset: set[str] = get_english_words_set(['web2'], lower=True)
    return [word for word in list(web2lowerset) if len(word) == n], [word for word in list(web2lowerset) if len(word) == n]



def compareGuessToWord(guessedWord, correctWord) -> str:
    listOfLetters: list[str] = []
    lettersInCorrectPlace: list[str] = []

    # checks for letters in the correct location
    for i in range(0, len(correctWord)):

        if guessedWord.lower()[i] == correctWord.lower()[i]:
            lettersInCorrectPlace.append(guessedWord.lower()[i])

    # checks the correct colour for each of the letters and adds them to listOfLetters: list[str]
    for i in range(0, len(correctWord)):

        if guessedWord.lower()[i] == correctWord.lower()[i]:
            listOfLetters.append(f"{GREEN}{guessedWord.upper()[i]}{OFF}")
        
        elif guessedWord.lower()[i] in correctWord.lower() and lettersInCorrectPlace.count(guessedWord.lower()[i]) < correctWord.count(guessedWord.lower()[i]):
            if listOfLetters.count(guessedWord.upper()[i]) < correctWord.count(guessedWord.lower()[i]):
                listOfLetters.append(f"{YELLOW}{guessedWord.upper()[i]}{OFF}")
            else:
                listOfLetters.append(f"{RED}{guessedWord.upper()[i]}{OFF}")

        else:
            listOfLetters.append(f"{RED}{guessedWord.upper()[i]}{OFF}")
        
    return "".join(listOfLetters)
            

def main() -> None:
    
    numberOfLetters: int = 0
    while numberOfLetters == 0:
        try:
            numberOfLetters: int = int(input("How many letters would you like your Wordle puzzle to be?: ").strip())
            wordToGuess: str = rchop(random.choice(createListOfNLetterWords(n = numberOfLetters)[1]), "\n")
            print(wordToGuess)
        except ValueError:
            print("Expected integer")

        except IndexError:
            print("Please choose a valid number of letters")

    
    guessesRemaining: int = GUESSES_PER_GAME
    guesses: list[str] = []

    while guessesRemaining >= 0:
        #print(f"{guess}\n" for guess in guesses)
        nextGuess = ""
        while len(nextGuess) != numberOfLetters or nextGuess not in createListOfNLetterWords(n=numberOfLetters)[0]:
            nextGuess = input()
            if len(nextGuess) != numberOfLetters:
                print(f"Your guess is too short/long! You need to guess a {numberOfLetters}-letter word!")
            elif nextGuess not in createListOfNLetterWords(n=numberOfLetters)[0]:
                print(f"That is not a valid word. Please try again.")

        guessesRemaining -= 1
        guesses.append(compareGuessToWord(guessedWord=nextGuess, correctWord=wordToGuess))
        print(compareGuessToWord(guessedWord=nextGuess, correctWord=wordToGuess))
        

if __name__ == "__main__":
    main()
