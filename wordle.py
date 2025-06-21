from english_words import get_english_words_set
import random

GUESSES_PER_GAME: int = 6

RED     =   "\033[1;31m"
YELLOW  =   "\033[1;33m"
GREEN   =   "\033[1;32m"
OFF     =   "\033[0;0m "

def createListOfNLetterWords(n) -> list:
    web2lowerset: set[str] = get_english_words_set(['web2'], lower=True)
    return [word for word in list(web2lowerset) if len(word) == n]

def compareGuessToWord(guessedWord, correctWord) -> str:
    listOfLetters = []
    for i in range(0, len(correctWord)):

        if guessedWord.lower()[i] == correctWord.lower()[i]:
            listOfLetters.append(f"{GREEN}{guessedWord.upper()[i]}{OFF}")

        elif guessedWord.lower()[i] in correctWord.lower():
            listOfLetters.append(f"{YELLOW}{guessedWord.upper()[i]}{OFF}")

        else:
            listOfLetters.append(f"{RED}{guessedWord.upper()[i]}{OFF}")
        
    return "".join(listOfLetters)
            

def main() -> None:
    
    numberOfLetters: int = 0
    while numberOfLetters == 0:
        try:
            numberOfLetters: int = int(input("How many letters would you like your Wordle puzzle to be?: ").strip())
            wordToGuess: str = random.choice(createListOfNLetterWords(n = numberOfLetters))
        except TypeError:
            print("Expected integer")
    
    guessesRemaining: int = GUESSES_PER_GAME
    guesses: list[str] = []

    while guessesRemaining >= 0:
        #print(f"{guess}\n" for guess in guesses)
        nextGuess = ""
        while len(nextGuess) != numberOfLetters:
            nextGuess = input()
        guessesRemaining -= 1
        guesses.append(compareGuessToWord(guessedWord=nextGuess, correctWord=wordToGuess))
        print(compareGuessToWord(guessedWord=nextGuess, correctWord=wordToGuess))
        

if __name__ == "__main__":
    main()
