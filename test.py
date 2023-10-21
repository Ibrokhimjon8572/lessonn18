# # nonlocal, lacal, global

# # global_value = 'base global version'
# # print(global_value)#1
# # def some_func():
# #     # global global_value
# #     global_value = 'new version'#2
# #     print(global_value)
# #     def inner():
# #         global global_value#2
# #         print(global_value)
# #         global_value = 'inner side'
# #         print(global_value)
# #     inner()
# #     print(global_value)
# # some_func()
# # print(global_value)
# # def a(b):
# #     def c(step=1):
# #         nonlocal b
# #         b += step
# #         print(b)
# #     return c

# # f = a(0)
# # f()
# # f(10)
# # f()
# # f()
# # f()
# # f()
# # f()
# # f()
# # def divider(y):
# # 	def divide(x):
# # 		return y / x
# # 	return divide

# # a = divider(20)

# # print(a(2))
# # print(a(3))
# # print(a(5))
# # print(a(7))
# # print(a(2))
# # print(a(10))
# # print(a(20))
# # print(a(1))

# # from collections import namedtuple

# # olma = namedtuple('olma', 'rang nav rang')
# # b = olma('qizil', 'Jannat', 'salom')
# # print(b.rang)
# # # b.rang = 'yashil'

# # print(b, type(b))
# # a = {1, 2, 3, 4, 5}
# # for i in range(1, 10):
# #     a.update({i})
# #     print(a)

# # a = 'olma'
# # b = {1,2,3}

# # print(dir(a))
# # print(dir(b))
# #  strings, lists, tuples, range objects
# # a = 'olma'
# # print(a[0])
# # a = dict()
# # b = list()
# # x = str()
# # ## for, in 

# # a = list()
# # a.clear()


# # if i in 
# class CustomIterableObject:
#     def __init__(self, end, step = 1, start = -100):
#         self._step = step
#         self._end = end
#         self._start = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self._start < self._end:
#             item = self._start
#             self._start += self._step
#             return item
#         else:
#             raise StopIteration
        
# b = range(1,2,3)
# print(dir(b))
# # for i in range(23, 2):
# #     print(i)
# # a = CustomIterableObject(10, 4, 2)
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())

# # class FibonacciIterator:
# #     def __init__(self, stop=10):
# #         self._stop = stop
# #         self._index = 0
# #         self._current = 0
# #         self._next = 1

# #     def __iter__(self):
# #         return self

# #     def __next__(self):
# #         if self._index < self._stop:
# #             self._index += 1
# #             fib_number = self._current
# #             self._current, self._next = (
# #                 self._next,
# #                 self._current + self._next,
# #             )
# #             return fib_number
# #         else:
# #             raise StopIteration

# # for i in FibonacciIterator(100):
# #     print(i)

# # def some_func():
# #     for i in range(1, 10):
# #         print(i)
# #         yield i

# # for i in some_func():
# #     print(i)
# # a = some_func()
# # print(a)
# range()

# class FileManager():
#     def __init__(self, filename, mode):
#         print('object yaratilyapti')
#         self.filename = filename
#         self.mode = mode
#         self.file = None
         
#     def __enter__(self):
#         print('men hozir enter ichidaman')
#         self.file = open(self.filename, self.mode)
#         return self.file
     
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print('men ishimni tugatdim')
#         self.file.close()
 
# # loading a file 
# with FileManager('test.txt', 'w') as f:
#     f.write('Test')
#     print('tugadi')

# print('out')
# print(f.closed)
# a = 11
# a = a + 11
# print(dir(a))