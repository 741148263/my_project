# for i in range(1, 21):
#     if i & 1:
#         print(i, end=" ")

import time

print('位与运算符与求余运算符判断奇偶数速度比拼')
r = range(10**7, 10**8)
t = time.perf_counter()
for i in r:
	if i & 1:
		pass
t1 = time.perf_counter() - t
print(f'位与耗时 {t1} 秒')

t = time.perf_counter()
for i in r:
	if i % 2 != 0:
		pass
t2 = time.perf_counter() - t
print(f'求余耗时 {t2} 秒')

print(f'位与是求余运算速度的 {t2/t1} 倍')

import time

print('左移运算符与乘法运算符运行速度比拼')
n = 123456789**10
r = range(10**7)
t = time.perf_counter()
for i in r:
	n << 10
t1 = time.perf_counter() - t
print(f'左移耗时 {t1} 秒')

t = time.perf_counter()
for i in r:
	n * 1024
t2 = time.perf_counter() - t
print(f'乘法耗时 {t2} 秒')

print(f'左移是乘法运算速度的 {t2/t1} 倍')