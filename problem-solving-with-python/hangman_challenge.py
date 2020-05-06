import random
import re

# Part1 - Playing a console-based game
# https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1124/handouts/200%20Assignment%204.pdf
class hangman:
    def __init__(self):
        self.index = random.randint(0, 9)
        self.word = self.getWord(self.index)

    def getWord(self, index):
        word = ''
        try:
            word = self.dict(index)
        except IndexError:
            print('getWord: Illegal index')
        return word

    def dict(self, index):
        words = {
            0: 'BUOY',
            1: 'COMPUTER',
            2: 'CONNOISSEUR',
            3: 'DEHYDRATE',
            4: 'FUZZY',
            5: 'HUBBUB',
            6: 'KEYHOLE',
            7: 'QUAGMIRE',
            8: 'SLITHER',
            9: 'ZIRCON'
        }
        return words[index]

    def playHangman(self, word):

        word_arr = list(word)
        secret_word = re.sub(r'[a-zA-z]', '-', word)
        secret_word_arr = list(secret_word)

        count = 8

        print('Welcome to Hangman!\n')
        while count > 0:

            print('The word now looks like this: ' + secret_word + '\n'
                  'You have ' + str(count) + ' guesses left.\n'
                  'Your guess: ')
            input_char = input().upper()

            if len(input_char) > 1:
                print("Please enter a single letter.")
            else:
                if input_char in word:
                    print('That guess is correct.')
                    word_index = [i for i, x in enumerate(word_arr) if x == input_char]
                    for i in range(len(secret_word_arr)):
                        if i in word_index:
                            secret_word_arr[i] = input_char
                    secret_word = ''.join(secret_word_arr)
                else:
                    print("There are no " + input_char + "'s in the word.")
                    count -= 1

                if secret_word == word:
                    print("You guessed the word: " + word + "\n"
                          "You win.")
                    break

        else:
            print("You're completely hung.\n"
                  "The word was: " + word + "\n"
                  "You lose.")

hm = hangman()
hm.playHangman(hm.word)