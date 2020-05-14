import random
import re
from turtle import *

# Part2 - Adding graphics
# https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1124/handouts/200%20Assignment%204.pdf
class hangman:
    def __init__(self):
        # 単語を選ぶ
        self.words_len = 10
        self.index = random.randint(0, self.words_len - 1)
        self.word = self.getWord(self.index)

        # キャンバスと描画用ペンを用意する
        self.setCanvas()
        self.drawing_pen = self.setDrawingPen()
        self.writing_pen = self.setWritingPen()
        self.font = font = ('terminal', 18, 'bold')

        # ハングマン描画用
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

    def setCanvas(self):
        Screen().setup(400, 700, 30, 30)
        # キャンバスをリセットする
        clearscreen()

    def setDrawingPen(self):
        drawing_pen = Turtle(visible=False)
        drawing_pen.speed('slowest')
        return drawing_pen

    def setWritingPen(self):
        writing_pen = Turtle(visible=False)
        writing_pen.speed('fastest')
        return writing_pen

    def writeText(self, secret_word, writing_pen):
        writing_pen.clear()
        writing_pen.penup()
        writing_pen.begin_fill()
        writing_pen.color('white')
        writing_pen.goto(-125, -200)
        writing_pen.pendown()
        writing_pen.fd(250)
        writing_pen.rt(90)
        writing_pen.fd(70)
        writing_pen.rt(90)
        writing_pen.fd(250)
        writing_pen.rt(90)
        writing_pen.fd(70)
        writing_pen.end_fill()

        writing_pen.penup()
        writing_pen.goto(0, -250)
        writing_pen.pendown()
        writing_pen.color('black')
        writing_pen.write(secret_word, font=self.font, align='center')

    def drawingHangman(self, count, drawing_pen):
        if count == 7:
            drawing_pen.left(90)
            # 亀のペンを上げて線を引かない。
            drawing_pen.penup()
            # 初期位置を設定
            drawing_pen.goto(-100, -150)
            # 亀のペンを下して線を引く。
            drawing_pen.pendown()
            drawing_pen.forward(self.scaffold_height)
        elif count == 6:
            drawing_pen.right(90)
            drawing_pen.forward(self.beam_length)
            drawing_pen.right(90)
            drawing_pen.forward(self.rope_length)
        elif count == 5:
            drawing_pen.right(90)
            drawing_pen.circle(self.head_radius)
            drawing_pen.penup()
            drawing_pen.circle(self.head_radius, 180)
            drawing_pen.pendown()
        elif count == 4:
            drawing_pen.right(90)
            drawing_pen.forward(self.body_length)
            # 後ずさる。
            drawing_pen.penup()
            drawing_pen.backward(self.body_length - self.arm_offset_from_head)
            drawing_pen.pendown()
        elif count == 3:
            drawing_pen.right(90)
            drawing_pen.forward(self.upper_arm_length)
            drawing_pen.left(90)
            drawing_pen.forward(self.lower_arm_length)
            # 後ずさる。
            drawing_pen.penup()
            drawing_pen.backward(self.lower_arm_length)
            drawing_pen.right(90)
            drawing_pen.backward(self.upper_arm_length)
            drawing_pen.pendown()
        elif count == 2:
            drawing_pen.backward(self.upper_arm_length)
            drawing_pen.left(90)
            drawing_pen.forward(self.lower_arm_length)
            # 後ずさる。
            drawing_pen.penup()
            drawing_pen.backward(self.lower_arm_length)
            drawing_pen.left(90)
            drawing_pen.backward(self.upper_arm_length)
            drawing_pen.right(90)
            drawing_pen.forward(self.body_length - self.arm_offset_from_head)
            drawing_pen.pendown()
        elif count == 1:
            drawing_pen.right(90)
            drawing_pen.forward(self.hip_width)
            drawing_pen.left(90)
            drawing_pen.forward(self.leg_length)
            drawing_pen.right(90)
            drawing_pen.forward(self.foot_length)
            drawing_pen.penup()
            drawing_pen.backward(self.foot_length)
            drawing_pen.right(90)
            drawing_pen.forward(self.leg_length)
            drawing_pen.right(90)
            drawing_pen.forward(self.hip_width)
            drawing_pen.pendown()
        elif count == 0:
            drawing_pen.forward(self.hip_width)
            drawing_pen.right(90)
            drawing_pen.forward(self.leg_length)
            drawing_pen.left(90)
            drawing_pen.forward(self.foot_length)
            drawing_pen.penup()
            drawing_pen.backward(self.foot_length)
            drawing_pen.left(90)
            drawing_pen.forward(self.hip_width)
            drawing_pen.home()
            drawing_pen.pendown()
            # ウィンドウをクリックしてゲームを終了させる
            Screen().exitonclick()

    def playHangman(self, word):
        word_arr = list(word)
        secret_word = re.sub(r'[a-zA-z]', '-', word)
        secret_word_arr = list(secret_word)

        count = 8

        print('Welcome to Hangman!')
        self.writeText(secret_word, self.writing_pen)

        while count > 0:
            print('The word now looks like this: ' + secret_word + '\n'
                  'You have ' + str(count) + ' guesses left.\n'
                  'Your guess: ')
            input_char = input().upper()

            # 1文字のみ入力できるようにする
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
                    # 文字列を表示する
                    self.writeText(secret_word, self.writing_pen)
                else:
                    print("There are no " + input_char + "'s in the word.")
                    count -= 1
                    # ハングマンを描く
                    self.drawingHangman(count, self.drawing_pen)
                # 勝ち
                if secret_word == word:
                    print("You guessed the word: " + word + "\n"
                          "You win.")
                    break
        # 負け
        else:
            print("You're completely hung.\n"
                  "The word was: " + word + "\n"
                  "You lose.")

hm = hangman()
hm.playHangman(hm.word)