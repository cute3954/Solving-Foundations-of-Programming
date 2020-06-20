# https://codingbat.com/prob/p238573
#
# Write a function that replaces the words in `raw` with the words in `code_words`
# such that the first occurrence of each word in `raw` is assigned the first unassigned word in `code_words`.
#
# encoder(["a"], ["1", "2", "3", "4"]) → ["1"]
# encoder(["a", "b"], ["1", "2", "3", "4"]) → ["1", "2"]
# encoder(["a", "b", "a"], ["1", "2", "3", "4"]) → ["1", "2", "1"]
def encoder(raw, code_words):
    strEncoder = {
        "a": code_words[0],
        "b": code_words[1],
        "c": code_words[2],
        "d": code_words[3]
    }

    result = []

    for str in raw:
        result.append(strEncoder[str])
    return result

raw = ["d", "b", "a", "d"]
code_words = ["1", "2", "3", "4"]
result = encoder(raw, code_words)
print(result)