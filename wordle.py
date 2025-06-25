from english_words import get_english_words_set
import random

GUESSES_PER_GAME: int = 6
RED     =   "\033[1;31m"    # For guessed letters that do not occur in the word
YELLOW  =   "\033[1;33m"    # For guessed letters that occur in the word, but are in the wrong place
GREEN   =   "\033[1;32m"    # For guessed letters that are in the correct place
OFF     =   "\033[0;0m "

def rchop(s: str, suffix: str) -> str:
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s


def createListOfNLetterWords(n: int=5) -> list:
    if n == 5:
        with open("guesses.txt", "r") as guesses:
            validGuesses: list[str] = [rchop(line, "\n") for line in guesses]
        with open("answers.txt", "r") as answers:
            validAnswers: list[str] = [rchop(line, "\n") for line in answers]

        return validGuesses, validAnswers

    web2lowerset: set[str] = get_english_words_set(['web2'], lower=True)
    return [word for word in list(web2lowerset) if len(word) == n], [word for word in list(web2lowerset) if len(word) == n]


def compareGuessToWord(guessedWord, correctWord) -> str:
    listOfLetters: list[str] = []
    lettersInCorrectPlace: list[str] = []

    # checks for any letters in the correct locations
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

    print("".join(listOfLetters))
    return guessedWord.upper() == correctWord.upper()
    
            

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

    while guessesRemaining > 0:
        nextGuess: str = ""
        while len(nextGuess) != numberOfLetters or nextGuess not in createListOfNLetterWords(n=numberOfLetters)[0]:
            nextGuess = input(f"Guess #{GUESSES_PER_GAME - guessesRemaining + 1}: ")
            if len(nextGuess) != numberOfLetters:
                print(f"Your guess is too short/long! You need to guess a {numberOfLetters}-letter word!")
            elif nextGuess not in createListOfNLetterWords(n=numberOfLetters)[0]:
                print(f"That is not a valid word. Please try again.")

        guessesRemaining -= 1

        if compareGuessToWord(guessedWord=nextGuess, correctWord=wordToGuess):
            print("Congratulations, you guessed the word correctly!")
            break
        

if __name__ == "__main__":
    main()
