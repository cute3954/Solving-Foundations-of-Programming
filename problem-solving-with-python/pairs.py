# https://codingbat.com/prob/p126332
#
# Given an array of non-empty strings, create and return a Map<String, String> as follows:
# for each string add its first character as a key with its last character as the value.
#
#
# pairs(["code", "bug"]) → {"b": "g", "c": "e"}
# pairs(["man", "moon", "main"]) → {"m": "n"}
# pairs(["man", "moon", "good", "night"]) → {"g": "d", "m": "n", "n": "t"}
def pairs(strings):
    result = {}
    for str in strings:
        firstStr = str[0]
        lastStr = len(str) - 1
        result[firstStr] = str[lastStr]
    return result

strings = ["man", "moon", "good", "night"]
result = pairs(strings)
print(result)