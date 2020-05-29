# 参照： https://codingbat.com/prob/p189576
# Consider the leftmost and rightmost appearances of some value in an array.
# We'll say that the "span" is the number of elements between the two inclusive.
# A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)
#
# maxSpan([1, 2, 1, 1, 3]) → 4
# maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
# maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

class maxSpan:
    def __init__(self):
        self.intArr = [1, 4, 2, 1, 4, 4, 4]

    def find_largest_span(self, intArr):
        max = 0
        for i in range(len(intArr)):
            j = len(intArr) - 1
            while intArr[i] != intArr[j]:
                # pythonで++とか--を入れると、エラーを吐く
                j-=1
            span = j - i + 1
            if span > max:
                max = span
        return max

max = maxSpan().find_largest_span(maxSpan().intArr)
print(max)