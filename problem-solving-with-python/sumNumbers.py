import re

# https://codingbat.com/prob/p121193
# Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)
#
# sumNumbers("abc123xyz") → 123
# sumNumbers("aa11b33") → 44
# sumNumbers("7 11") → 18

class SumNumbers:
    def findInteger(self, str):
        # 文字列の配列を数値の配列に変換
        numArr = list(map(int, re.findall("\d+", str)))
        # リスト要素の合計を計算する
        total = sum(numArr)
        return total
sumNums = SumNumbers()
total = sumNums.findInteger("7 11")
print(total)

