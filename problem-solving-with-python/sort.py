# https://codingbat.com/prob/p262890
# Return an array that contains the sorted values from the input array with duplicates removed.
#
# sort([]) → []
# sort([1]) → [1]
# sort([1, 1]) → [1]
def sort(int_arr):
    # dict.fromkeys(): 引数に指定したシーケンス型（リストやタプルなど）をキーとして新たな辞書オブジェクトを生成する。
    # 辞書のキーは重複した要素を持たないため、set()と同じく重複する値は無視される。
    # 元のリストの順序を保持する
    return list(dict.fromkeys(int_arr))

int_arr = [1, 1]
result = sort(int_arr)
print(result)