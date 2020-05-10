import random
import re
from turtle import *

# Part2 - Adding graphics
# https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1124/handouts/200%20Assignment%204.pdf
class hangman:
    def __init__(self):
        self.words_len = 10
        self.index = random.randint(0, self.words_len - 1)
        self.word = self.getWord(self.index)

        self.scaffold_height = 360
        self.beam_length = 144
        self.rope_length = 18
        self.head_radius = 36
        self.body_length = 144
        self.arm_offset_from_head = 28
        self.upper_arm_length = 72
        self.lower_arm_length = 44
        self.hip_width = 36
        self.leg_length = 108
        self.foot_length = 28

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

    def drawingHangman(self, count):
        wn = Screen()
        wn.setup(400, 600, 30, 30)
        clearscreen()
        if count == 7:
            left(90)
            # 亀のペンを上げて線を引かない。
            penup()
            # 初期位置を設定
            goto(-100, -200)
            # 亀のペンを下して線を引く。
            pendown()
            forward(self.scaffold_height)
        elif count == 6:
            right(90)
            forward(self.beam_length)
            right(90)
            forward(self.rope_length)
        elif count == 5:
            right(90)
            circle(self.head_radius)
            penup()
            circle(self.head_radius, 180)
            pendown()
        elif count == 4:
            right(90)
            forward(self.body_length)
            # 後ずさる。
            penup()
            backward(self.body_length - self.arm_offset_from_head)
            pendown()
        elif count == 3:
            right(90)
            forward(self.upper_arm_length)
            left(90)
            forward(self.lower_arm_length)
            # 後ずさる。
            penup()
            backward(self.lower_arm_length)
            right(90)
            backward(self.upper_arm_length)
            pendown()
        elif count == 2:
            backward(self.upper_arm_length)
            left(90)
            forward(self.lower_arm_length)
            # 後ずさる。
            penup()
            backward(self.lower_arm_length)
            left(90)
            backward(self.upper_arm_length)
            right(90)
            forward(self.body_length - self.arm_offset_from_head)
            pendown()
        elif count == 1:
            right(90)
            forward(self.hip_width)
            left(90)
            forward(self.leg_length)
            right(90)
            forward(self.foot_length)
            penup()
            backward(self.foot_length)
            right(90)
            forward(self.leg_length)
            right(90)
            forward(self.hip_width)
            pendown()
        elif count == 0:
            forward(self.hip_width)
            right(90)
            forward(self.leg_length)
            left(90)
            forward(self.foot_length)
            penup()
            backward(self.foot_length)
            left(90)
            forward(self.hip_width)
            home()
            pendown()
            # ウィンドウをクリックしてゲームを終了させる
            wn.exitonclick()

    def playHangman(self, word):

        word_arr = list(word)
        secret_word = re.sub(r'[a-zA-z]', '-', word)
        secret_word_arr = list(secret_word)

        count = 8

        print('Welcome to Hangman!')
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
                    self.drawingHangman(count)
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