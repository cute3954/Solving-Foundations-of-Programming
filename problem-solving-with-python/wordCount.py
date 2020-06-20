# https://codingbat.com/prob/p117630
#
# The classic word-count algorithm: given an array of strings,
# return a Map<String, Integer> with a key for each different string,
# with the value the number of times that string appears in the array.
#
# wordCount(["a", "b", "a", "c", "b"]) → {"a": 2, "b": 2, "c": 1}
# wordCount(["c", "b", "a"]) → {"a": 1, "b": 1, "c": 1}
# wordCount(["c", "c", "c", "c"]) → {"c": 4}

from collections import Counter

def countWords(strings):
    # Counterについて
    # 参考：https://qiita.com/kenta1984/items/5b61ecc4b96a30a32601

    # 辞書の初期化
    result = Counter()

    for str in strings:
        result[str] += 1

    # Counterはdictまたはそのサブクラスであり、
    # マッピングはdictに渡すことができる。
    return dict(result)

strings = ["c", "b", "a", "a", "c"]
result = countWords(strings)
print(result)