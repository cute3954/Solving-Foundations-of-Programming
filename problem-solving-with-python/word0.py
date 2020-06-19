# https://codingbat.com/prob/p152303
#
# Given an array of strings, return a Map<String, Integer> containing a key
# for every different string in the array, always with the value 0.
# For example the string "hello" makes the pair "hello":0.
# We'll do more complicated counting later, but for this problem the value is simply 0.
#
# word0(["a", "b", "a", "b"]) → {"a": 0, "b": 0}
# word0(["a", "b", "a", "c", "b"]) → {"a": 0, "b": 0, "c": 0}
# word0(["c", "b", "a"]) → {"a": 0, "b": 0, "c": 0}
def word0(strings):
    result = {}
    for str in strings:
        result[str] = 0
    return result

strings = ["a", "b", "a", "c", "b"]
result = word0(strings)
print(result)