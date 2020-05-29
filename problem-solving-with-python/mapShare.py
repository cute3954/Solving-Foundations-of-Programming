# https://codingbat.com/prob/p148813
# Modify and return the given map as follows: if the key "a" has a value,
# set the key "b" to have that same value. In all cases remove the key "c",
# leaving the rest of the map unchanged.

# mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
# mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
# mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}

def mapShare(map):
    if "a" in map:
        map["b"] = map.get("a")
    if "c" in map:
        map.pop("c")
    result = map
    return result

map = {
    "a": "xyz",
    "b": "1234",
    "c": "yo",
    "d": "ddd",
    "e": "everything"
        }
result = mapShare(map)
# {'a': 'xyz', 'b': 'xyz', 'd': 'ddd', 'e': 'everything'}
print(result)