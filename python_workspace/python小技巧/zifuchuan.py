# python 之字符串和文本处理

# string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有多个分隔符或者是分隔符周围不确定的空格。
# 当你需要更加灵活的切割字符串的时候，最好使用re.split()方法
import sys

line = 'asdf fjdk; afed, fjek,asdf, foo'

import re

# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
split_line_list = re.split(r"[;,\s]\s*", line)
print(split_line_list)

# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
split_line_list = re.split(r"(;|,|\s)\s*", line)
print(split_line_list)

split_line_list = re.split(r'(?:,|;|\s)\s*', line)
print(split_line_list)

# 检查字符串的开头和结尾
# 检查字符串开头或结尾的一个简单方法是使用str.startswith()或者是str.endswith()方法
# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传给 startswith() 或者 endswith() 方法
import os

filenames = os.listdir(".")
print([name for name in filenames if name.endswith((".yaml", ".sh", ".pdf", ".py"))])
print(any(name.endswith(".py") for name in filenames))
# 必须要输入一个元组作为参数。如果你恰巧有一个 list 或者 set 类型的选择项，要确保传递参数前先调用 tuple() 将其转换为元组类型


# 字符串的替换，简单的模式使用str.replace("旧", "新")
# 复杂的模式，请使用 re 模块中的sub()函数。sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如 \3 指向前面模式的捕获组号。
data = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', 'Today is 11/27/2012. PyCon starts 3/13/2013.')
print(data)

from calendar import month_abbr

text = "Today is 11/27/2012. PyCon starts 3/13/2013."
pattern = re.compile(r"(\d+)/(\d+)/(\d+)")


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return "{} {} {}".format(m.group(2), mon_name, m.group(3))


data = pattern.sub(change_date, text)
new_data, n = pattern.subn(change_date, text)
print(data)
print(new_data, n)

# 字符串忽略大小写的搜索替换
text = 'UPPER PYTHON, lower python, Mixed Python'
data = re.findall("python", text, flags=re.IGNORECASE)
print(data)
data = re.sub("python", "java", text, flags=re.IGNORECASE)
print(data)


# 替换字符串并不会自动跟被匹配字符串的大小写保持一致。为了修复这个，你可能需要一个辅助函数
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


data = re.sub("python", matchcase("java"), text, flags=re.IGNORECASE)
print(data)

# 定义实现最短匹配的正则表达式
# 用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。而你想修改它变成查找最短的可能匹配。
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
# 正则表达式中 * 操作符是贪婪的，因此匹配操作会查找最长的可能匹配,可以在模式中的 * 操作符后面加上? 修饰符,使得匹配变成非贪婪模式
# 点 (.) 匹配除了换行外的任何字符,如果你将点 (.) 号放在开始与结束符 (比如引号) 之间的时候，那么匹配操作会查找符合模式的最长可能匹配,在 * 或者 + 这样的操作符后面添加一个?可以强制匹配算 法改成寻找最短的可能匹配。


name = "Mrs Gao"

n = 10

# 如果要被替换的变量能在变量域中找到，那么你可以结合使用 format map()和 vars()
print("Your name is {name}, has {n} messages".format_map(vars()))


# vars() 还有一个有意思的特性就是它也适用于对象实例


class Info():
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info("Osk", 20)
print("Your name is {name}, has {n} messages".format_map(vars(a)))


class SafeSub(dict):
    def __missing__(self, key):
        return "{" + key + "}"

def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))

# sys._getframe:返回来自调用栈的一个帧对象。如果传入可选整数 depth，则返回从栈顶往下相应调用层数的帧对象。如果该数比调用栈更深，则抛出 ValueError。depth 的默认值是 0，返回调用栈顶部的帧。sys. getframe(1) 返回调用者的栈帧，可以从中访问属性 f_locals 来获得局部变量,
# f_locals 是一个复制调用函数的本地变量的字典。尽管你可以改变 f_locals 的内容，但是这个修改对于后面的变量访问没有任何影响。所以，虽说访问一个栈帧看上去很邪恶，但是对它的任何操作不会覆盖和改变调用者本地变量的值。

print(sub('Your favorite color is {color}'))


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

# text = ''.join(sample())
# print (text)
b = sample()

while True:
    try:
        print(next(b))
    except StopIteration:
        print("迭代器已经取完了")
        break


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))

s = 'pýtĥöñ\fis\tawesome\r\n'

remap = {
    ord("\t"): " ",
    ord("\f"): " ",
    ord("\r"): None,
}
print(s)
print(s.translate(remap))

import unicodedata

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize("NFD", s)
print(b)
print(b.translate(cmb_chrs))
