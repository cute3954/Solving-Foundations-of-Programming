# 参照：　https://codingbat.com/prob/p117334
# Given a non-empty string like "Code" return a string like "CCoCodCode".

# stringSplosion("Code") → "CCoCodCode"
# stringSplosion("abc") → "aababc"
# stringSplosion("ab") → "aab"

class stringSplosion:
    def __init__(self):
        self.str = 'There'

    def stringSplosion(self, str):
        # strを1文字ずつのリストにする
        strArray = list(str)
        # 新しい文字列を格納する変数
        createNewWord = '';
        # 配列の長さ
        for i in range(0, len(strArray) + 1):
            for j in range(0, i):
                createNewWord = createNewWord + strArray[j]
        return createNewWord

strSpl = stringSplosion()
newWord = strSpl.stringSplosion(strSpl.str)
print(newWord)