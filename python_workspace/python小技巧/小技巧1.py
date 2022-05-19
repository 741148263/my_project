# 列表中出现次数最多的元素
import sys
import time

test_list = [9, 9, 6, 5, 2, 3, 4, 5, 6, 5, 4, 52, 6, 3]
most_frequent_element = max(set(test_list), key=test_list.count)

# 用键值对字典进行排序
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

# 移除字符串的的数字
msg = "".join(list(filter(lambda c: c.isalpha(), "fajkfj1521fda54fd3a1f23d15a41f3da")))

# 矩阵变换
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result1 = list(list(i) for i in zip(*old_list))

# 拷贝文件
import shutil

# shutil.copyfile("小技巧1.py", "小技巧1_copy.py")

# 列表中最长的字符串
words = ["this", "is", "a", "list", "of", "words"]
result2 = max(words, key=len)
print(result2)

# 检查数据类型
print(isinstance(2, int))


# map函数 map(function, iterables)
# Map是程序员用来简化程序的Python内置函数,此函数可以在不使用任何循环的情况下对所有指定的元素进行迭代
def add_list(a, b):
    return a + b


output = list(map(add_list, [1, 2, 3], [4, 5, 6]))
print(output)


# ilter是Python中的另一个内置函数，当需要区分其他类型的数据时，这个函数非常有用。Filter函数经常用于根据特定过滤条件来提取数据

def is_positive(a):
    return a > 0


result3 = list(filter(is_positive, [1, -2, 3, -4, 5, -6]))
print(result3)

import functools


# 当需要对给定列表中的所有元素使用相同的操作时使用Reduce函数。
def sum_two_elements(a, b):
    return a + b


numbers = [6, 2, 1, 3, 4]
result4 = functools.reduce(sum_two_elements, numbers)
print(result4)

# 显示进度条
# 1. 普通进度条
for i in range(1, 101):
    print("\r", end="")
    print("进度: {}%: ".format(i), "▓" * (i // 2), end="")
    sys.stdout.flush()
    time.sleep(0.05)

# 带时间的普通进度条
t = 60
print("**************带时间的进度条**************")
start = time.perf_counter()
for i in range(t + 1):
    finsh = "▓" * i
    need_do = "-" * (t - i)
    progress = (i / t) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
    time.sleep(0.05)

print()
# 多种样式的格式化输出
print("{:{fill_str}{align}10}".format("good", fill_str="0", align="<"))
print("{0:0<8}".format("hello"))
print("{0:0^8}".format("hello"))
print("{0:0>8}".format("world"))
str1 = "hello"
print(str1.ljust(10, "0"))
print(str1.rjust(10, "0"))



# 一行代码求多个列表的最大值
print(max(max([1,2,3,4],[5,1,3,9],[3], key=lambda v:max(v))))