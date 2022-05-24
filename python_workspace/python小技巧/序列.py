import array
import bisect

# 计算笛卡尔积
colors = ["black", "white"]
sizes = ["S", "M", "L"]
# 列表推导式
tshirts = [(color, size) for color in colors for size in sizes]
# <class 'list'> [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
print(type(tshirts), tshirts)
# 生成器表达式
tshirts_generator = ((color, size) for color in colors for size in sizes)
# <class 'generator'> ('black', 'S')
print(type(tshirts_generator), next(tshirts_generator))

"""
Tips:
    生成器表达式逐个产出元素，从来不会一次性产出所有元素的列表
"""

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'
"""
bisect.bisect_left(有序序列, 插入元素)， 返回索引
"""
print(bisect.bisect_left(HAYSTACK, 25))
# 插入, 效率比insert要高
print(bisect.insort(HAYSTACK, 25))
print(HAYSTACK)

print("-"*30)
# 共享内存，修改值
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(numbers[0])
print(memv[0])
memn_oct = memv.cast("B")
print(memn_oct.tolist())
memn_oct[5] = 4
print(numbers)

import itertools

# 无限迭代器： count, cycle, repeat

# cycle() 用于对 iterable 中的元素反复执行循环：
cycle_strings = itertools.cycle("ABC")
i = 1
for string in cycle_strings:
    if i == 10:
        break
    print(i, string)
    i += 1

# 迭代器的特点是：惰性求值（Lazy evaluation），即只有当迭代至某个值时，它才会被计算，这个特点使得迭代器特别适合于遍历大文件或无限集合等，因为我们不用一次性将它们存储在内存中
print("-"*30)
# count() 接收两个参数，第一个参数指定开始值，默认为 0，第二个参数指定步长，默认为 1
nums = itertools.count()
for i in nums:
    if i > 6:
        break
    print(i)

nums = itertools.count(10, 2)
for i in nums:
    if i > 30:
        break
    print(i)

# repeat() 用于反复生成一个 object

for item in itertools.repeat("hello world", 3):
    print(item)

# 有限迭代器
# chain()， compress, dropwhile, groupby, ifilter, ifilterfalse, islice, imap, starmap, tee, takewhile,izip, izip_longest

# chain 接收多个可迭代对象作为参数，将它们『连接』起来，作为一个新的迭代器返回
for item in itertools.chain([1,2,3], ["a", "b", "c"]):
    print(item)
# chain 接收一个可迭代对象作为参数，返回一个迭代器：
string = itertools.chain.from_iterable("ABCD")
print(next(string))

# compress 可用于对数据进行筛选，当 selectors 的某个元素为 true 时，则保留 data 对应位置的元素，否则去除：
# ['A', 'B', 'D', 'F']
print(list(itertools.compress("ABCDEF", [1,1,0,1,0,1])))

# dropwhile(predicate, iterable) predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则丢弃该元素，否则返回该项及所有后续项。
# [5, 6, 7, 1, 2]
print(list(itertools.dropwhile(lambda x:x<5, [1,3,5,6,7,1,2])))
print(list(itertools.dropwhile(lambda x: x > 3, [2, 1, 6, 5, 4])))

print("-"*30)
# groupby 用于对序列进行分组，它的使用形式如下：groupby(iterable[, keyfunc])
# 其中，iterable 是一个可迭代对象，keyfunc 是分组函数，用于对 iterable 的连续项进行分组，如果不指定，则默认对 iterable 中的连续相同项进行分组，返回一个 (key, sub-iterator) 的迭代器

for key, value in itertools.groupby("aaaabbbcccacd"):
    # a : ['a', 'a', 'a', 'a']
    # b : ['b', 'b', 'b']
    # c : ['c', 'c', 'c']
    # a : ['a']
    # c : ['c']
    # d : ['d']
    print(key, ":", list(value))
print("-"*30)
data = ["a", "bb", "cc", "dd", "eee", "f"]
for key, value in itertools.groupby(data, len):
    # 1 : ['a']
    # 2 : ['bb']
    # 3 : ['ccc']
    # 2 : ['dd']
    # 3 : ['eee']
    # 1 : ['f']
    print(key, ":", list(value))
print("-"*30)
# islice 是切片选择，它的使用形式如下: islice(iterable, [start,] stop [, step]).iterable 是可迭代对象，start 是开始索引，stop 是结束索引，step 是步长，start 和 step 可选。
print(list(itertools.islice([10, 6, 2, 8, 1, 3, 9], 5)))

from itertools import tee

# tee 的使用形式如下：tee(iterable [,n])tee 用于从 iterable 创建 n 个独立的迭代器，以元组的形式返回，n 的默认值是 2。

print(tee("abcd"))
it1, it2 = tee("abcde")
# ['a', 'b', 'c', 'd', 'e'] ['a', 'b', 'c', 'd', 'e']
print(list(it1), list(it2))


# takewhile: takewhile(predicate, iterable),predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则保留该元素，只要 predicate(item) 为 false，则立即停止迭代。
# [1, 2, 3, 4]
print(list(itertools.takewhile(lambda x:x<5, [1,2,3,4,5,6])))
# []
print(list(itertools.takewhile(lambda x: x > 3, [2, 1, 6, 5, 4])))

# 组合生成器product， permutations, combinations, combinations_with_replacement

print("-"*30)
# product 用于求多个可迭代对象的笛卡尔积，它跟嵌套的 for 循环等价
# product(iter1, iter2, ... iterN, [repeat=1])
for item in itertools.product("ABCD", "xy", "cds"):
    print(item)

print(list(itertools.product("ABC", repeat=2)))
print(list(itertools.product("ABC", "ABC")))

# permutations 用于生成一个排列，它的一般使用形式如下permutations(iterable[, r])r 指定生成排列的元素的长度，如果不指定，则默认为可迭代对象的元素长度
print("-"*30)
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
print(list(itertools.permutations("ABCD", 2)))

# combinations用于求序列的组合，它的使用形式如下：combinations(iterable, r)r 指定生成组合的元素的长度
print(list(itertools.combinations([10,20,30,40,50,60], 2)))


print("-"*30)
data = {"01": [1,2,3,4,5], "02": [1,2,3,4,5], "03": [1,2,3,4,5]}
iters = iter(data)
for i in itertools.islice(iters, 1):
    print(i)