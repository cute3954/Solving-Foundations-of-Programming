class dictionary:
    # returnがいらない
    def __init__(self):
        self.S = 'abppplee'
        self.D = ['able', 'ale', 'apple', 'bale', 'kangaroo']

    def find_longest_st(self, S, D):
        # ['kangaroo', 'apple', 'able', 'bale', 'ale']
        D = sorted(D, key=len, reverse=True)
        for word in D:
            i = j = 0
            while True:
                try:
                    # index(): 引数に調べたい値を指定するとインデックスが取得できる
                    i += S[i:].index(word[j])
                    j += 1
                # ValueError: 引数の型はあっているけれど誤った値をとっている場合に発生する
                # 例外をキャッチする
                # ここではサブシーケンス（S）じゃない場合, whileから抜け出す
                except ValueError:
                    break
                # IndexError: シーケンスの添え字が範囲外の場合に発生する
                # ここではWをリターンする
                except IndexError:
                    return word

# インスタンス化
dict = dictionary()
# メソッド実行
W = dict.find_longest_st(dict.S, dict.D)
# wを出力する
# apple
print(W)





