#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#-----------------------------进程----------------------------
import os
os.getpid() # 拿到当前进程ID
os.getppid() # 拿到父进程的ID

# Unix/Linux操作系统提供了一个fork()系统调用
# fork() 把当前进程（称为父进程）复制一份（称为子进程）若成功调用一次则返回两个值，
# 子进程返回0，父进程返回子进程标记；否则，出错返回-1。
pid = os.fork()


# Python的os模块封装了常见的系统调用，其中就包括fork
# 在Python程序中创建子进程
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


#-----------------------------multiprocessing----------------------------
# multiprocessing模块提供了一个Process类来代表一个进程对象

# 启动一个子进程并等待其结束
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) # 创建一个Process实例
    print('Child process will start.')
    p.start() # 启动
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')


# Pool 进程池
# 批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# TODO