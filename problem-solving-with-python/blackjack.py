# https://codingbat.com/prob/p117019
#
# Given 2 int values greater than 0, return whichever value is nearest to 21 without going over.
# Return 0 if they both go over.
#
# blackjack(19, 21) → 21
# blackjack(21, 19) → 21
# blackjack(19, 22) → 19
def blackjack(a, b):
    result = 0

    if a > 21 and b > 21:
        return result
    else:
        if a >= b:
            # pythonで三項演算子を作成する方法
            # https://qiita.com/howmuch515/items/bf6d21f603d9736fb4a5
            result = a if a <= 21 else b
        else:
            result = b if b <= 21 else a

    return result

result = blackjack(22, 22)
print(result)