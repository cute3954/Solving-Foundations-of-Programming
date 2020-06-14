# 辞書（連想配列、ハッシュテーブル）

# 参考
# https://docs.python.org/ja/3/tutorial/datastructures.html#dictionaries
# https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
# https://wikidocs.net/16
# https://wikidocs.net/16043
# https://qiita.com/tenten1010/items/da4084f937ad07e70164

import copy
from pprint import pprint as pp

# 波括弧で辞書を作成する。
d = {}
print(type(d)) # <class 'dict'>
# dict型のコンストラクタで辞書を作成
e = dict()
print(type(e)) # <class 'dict'>

# キーとしてimmutableな型（再代入が不可能なオブジェクト）は使える。
d = {(1, 5): 5, (3, 3): 3} # tuple
d = {3.6: 5, 'abc': 3} # float
d = {True: 5, 'abc': 3} # bool
print(d)

# mutableな型（再代入可能なオブジェクト）は使えない。
# d = {{1, 3}: 5, {3, 5}: 3} # TypeError: unhashable type: 'set'
# d = {[1, 3]: 5, [3, 5]: 3} # TypeError: unhashable type: 'list'
# d = {{"a": 1}: 5, 'abc': 3} # TypeError: unhashable type: 'dict'

# キーが重複する場合、上書きされる。
print({'a': 1, 'a': 2})

d = {'abc': 1, 'def': 2}
# キーでインデックス化されており、整数で値を取得できない。
# print(d[0]) # KeyError: 0
print(d['abc'])

# キーを指定して要素の値を変更することができる。
d['abc'] = 5
# 新しい要素を追加できる。
d['ghi'] = 999
print(d)

newdict = dict(alice = 5, bob = 20, tony = 15, suzy = 30)
print(newdict)

# リストから辞書を作成できる。
name_and_ages = [['alice', 5], ['bob', 13]] # リストの要素がすでに2個組のリストとなっている
print(dict(name_and_ages))
name_and_ages = [('alice', 5), ('bob', 13)] # リストの要素がすでに2個組のタプルとなっている
print(dict(name_and_ages))
# タプルから辞書を作成できる。
name_and_ages = (('alice', 5), ('bob', 13)) # タプルの要素がすでに2個組のタプルとなっている
print(dict(name_and_ages))
name_and_ages = (['alice', 5], ['bob', 13]) # タプルの要素がすでに2個組のリストとなっている
print(dict(name_and_ages))

# コピー
# 参考: https://qiita.com/Kaz_K/items/a3d619b9e670e689b6db
# 浅いコピー（shallow copy）
a = {'alice': [1,2,3], 'bob': 20, 'tony': 15, 'suzy': 30}
b = a.copy()
b['alice'].append(5)
print(b)
print(a)

a = {'alice': [1,2,3], 'bob': 20, 'tony': 15, 'suzy': 30}
b = dict(a)
print(a)
print(b)
print(id(a))
print(id(b))

# 深いコピー（deep copy）
# コピーした辞書を別々の辞書として扱うため利用する。
a = {'alice': [1,2,3], 'bob': 20, 'tony': 15, 'suzy': 30}
b = copy.deepcopy(a)
b['alice'].append(5)
print(b)
print(a)

# 要素の値を変更する。
a = {'alice': [1,2,3], 'bob': 20, 'tony': 15, 'suzy': 30}
# キーを指定して新しい値を代入する。
a['alice'] = 5
print(a)

a = {'alice': [1,2,3], 'bob': 20, 'tony': 15, 'suzy': 30}
# 複数の要素を追加・更新
a.update({'bob': 99, 'tony': 99, 'kim': 30})
# 要素を削除
del a['alice']
print(a)

# forループ処理
# 参考: https://note.nkmk.me/python-dict-keys-values-items/
a = {'alice': [1,2,3], 'bob': 20, 'tony': 15, 'suzy': 30}
# 辞書オブジェクトをそのままfor分で回すとキーが取得できる。
for key in a: # for key in a.keys():も可能
    print(key)
for val in a.values():
    print(val)
# 各要素のキーと値の両方に対してforループ処理を行う。
for key, val in a.items():
    print('key={key}, value={value}'.format(key=key, value=val))

# 指定のキーの要素が辞書の中に含まれているかどうかを確認する。
print('alice' in a)
print('teacher' not in a)

a = {'alice': [1,2,3], 'bob': 20, 'tony': 15, 'suzy': 30, 'dodo': [1, 3, 5, 7], 'mario': 'pitch'}
# 以下のように辞書の要素ごとに改行されて見やすくなる。
# なお、辞書の要素はキーの順番でソートされる。
# {'alice': [1, 2, 3],
#  'bob': 20,
#  'dodo': [1, 3, 5, 7],
#  'mario': 'pitch',
#  'suzy': 30,
#  'tony': 15}
pp(a)

l = [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]},
     {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]},
     {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

# 出力幅を指定する。
# [{'Age': 40,
#   'Name': 'Alice XXX',
#   'Points': [80, 20]},
#  {'Age': 20,
#   'Name': 'Bob YYY',
#   'Points': [90, 10]},
#  {'Age': 30,
#   'Name': 'Charlie ZZZ',
#   'Points': [70, 30]}]
pp(l, width=40)

# help(d)