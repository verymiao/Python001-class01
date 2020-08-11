#作业一：
"""
容器序列: list, tuple, dict
扁平序列: str, collections.deque

可变序列: list, dict
不可变序列: str, tuple, collections.deque
"""


#作业二:
#python2 映射功能
def mymap2(func,list1):
    if list1 == []:
        return []
    else:
        return [func(list1[0])] + mymap2(func,list1[1:])

#python3 生成器
def mymap3(func,list1):
    num = 0
    for i in list1:
        yield func(list1[num])
        num += 1


#测试
def duble(x):
    return x*2
li = [x for x in range(10)]
li2 = mymap2(duble,li)
print(li2)

li3 = mymap3(duble,li)
print(li3)
for i in li3:
    print(i)


# import unittest
# class TestMap(unittest.TestCase):
#     def




#作业三
import time
def timer(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(f'{func.__name__}运行时间: {end_time - start_time}')
    return wrapper

@timer
def test1(s):
    time.sleep(s)

test1(3)




