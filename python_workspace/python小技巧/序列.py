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
