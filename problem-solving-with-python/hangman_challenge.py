import random
import re

# Part1 - Playing a console-based game
# https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1124/handouts/200%20Assignment%204.pdf
class hangman:
    def __init__(self):
        # 単語数
        self.words_len = 10
        # 0 - 9の範囲内ランダムな整数を返す。
        self.index = random.randint(0, self.words_len - 1)
        # indexを指定して単語を取得する。
        self.word = self.getWord(self.index)

    def getWord(self, index):
        word = ''
        try:
            word = self.dict(index)
        # indexが範囲外の場合
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
        # reについて
        # https://docs.python.org/ja/3/library/re.html
        # 正規表現でアルファベットを「-」に置換
        secret_word = re.sub(r'[a-zA-z]', '-', word)
        secret_word_arr = list(secret_word)

        count = 8

        print('Welcome to Hangman!')
        while count > 0:
            print('The word now looks like this: ' + secret_word + '\n'
                  'You have ' + str(count) + ' guesses left.\n'
                  'Your guess: ')
            # もし小文字を入力しても、大文字に変換してくれる。
            input_char = input().upper()

            if len(input_char) > 1:
                print("Please enter a single letter.")
            else:
                if input_char in word:
                    print('That guess is correct.')
                    # リストから入力した文字列と同じ要素のインデックスを全部取得。
                    word_index = [i for i, x in enumerate(word_arr) if x == input_char]
                    # 当てた文字列のみ「-」をアルファベットに置換。
                    for i in range(len(secret_word_arr)):
                        if i in word_index:
                            secret_word_arr[i] = input_char
                    secret_word = ''.join(secret_word_arr)
                else:
                    print("There are no " + input_char + "'s in the word.")
                    count -= 1

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