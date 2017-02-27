#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-26 21:35:23
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 序列化
# import json


# class Student(object):

#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score

#     def sudent2dict(std):
#         return{
#             'name': std.name,
#             'age': std.age,
#             'score': std.score
#         }

# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))

# 进程
# import os

# print 'Process(%s)start...' % os.getpid()
# pid = os.fork()
# if pid == 0:
#     print 'I am child process(%s)and my parent is %s.' \
#         % (os.getpid(), os.getppid())
# else:
#     print 'I(%s)just created a child process (%s).' % (os.getpid(), pid)

# from multiprocessing import Process
# import os

# # 子进程要执行的代码


# def run_proc(name):
#     print 'Run child process %s(%s)...' % (name, os.getpid())

# if __name__ == '__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Process(target=run_proc, args=('test,'))
#     print 'Process will start.'
#     p.start()
#     p.join()
#     print 'process end.'

# 多进程
# from multiprocessing import Pool
# import os
# import time
# import random


# def long_time_task(name):
#     print 'Run task %s(%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.' % (name, (end-start))

# if __name__ == '__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'

# from multiprocessing import Process, Queue
# import os
# import time
# import random

# # 写数据进程执行的代码


# def write(q):
#     for value in ['A', 'B', 'C']:
#         print 'Put %s to queue...' % value
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码


# def read(q):
#     while True:
#         value = q.get(True)
#         print 'Get %s from queue.' % value

# if __name__ == '__main__':
#     # 父进程创建Queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw,写入
#     pw.start()
#     # 启动子进程pr,读取
#     pr.start()
#     # 等待pw结束：
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止：
#     pr.terminate()


# 多线程
import time
import threading

# 新线程执行的代码


#def loop():
#   print 'thread %s is running...' % threading.current_thread().name
#   n = 0
#   while n < 5:
#       n = n+1
#       print 'thread %s >>> %s' % (threading.current_thread().name, n)
#       time.sleep(1)
#   print 'thread %s ended.' % threading.current_thread().name
#
#print 'thread %s is running...' % threading.current_thread().name
#t = threading.Thread(target=loop, name='LoopThread')
#t.start()
#t.join()
#print 'thread %s ended.' % threading.current_thread().name
