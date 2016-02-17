# -*- coding: utf-8 -*-
"""
singleton.py
------------
单例 
是最为最常见的设计模式之一。对于任何时刻，如果某个类只存在且最多存在一个具体的实例，那么我们称这种设计模式为单例。
例如，对于 class Mouse (不是动物的mouse哦)，我们应将其设计为 singleton 模式。
你的任务是设计一个 getInstance 方法，对于给定的类，每次调用 getInstance 时，都可得到同一个实例。

样例:
在 Java 中:
A a = A.getInstance();
A b = A.getInstance();
a 应等于 b.

挑战:
如果并发的调用 getInstance，你的程序也可以正确的执行么？

参考:
1.线程安全的Java实现:http://www.cnblogs.com/EdwardLiu/p/4443230.html
2.A thread safe implementation of singleton pattern in Python. 
Based on tornado.ioloop.IOLoop.instance() approach.
3.http://stackoverflow.com/questions/21978977/whether-the-method-below-is-thread-safe-when-implementing-singleton-pattern-in-p
4.https://morkrispil.wordpress.com/2013/06/02/singleton-pattern-for-python-single-and-multi-threaded/
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 17,2016
"""
import threading, time, random
class Solution:
    #hide class variable with "__" prefix
    __singleton_instance = None
    #create lock object
    __singleton_lock = threading.Lock()
    
    @classmethod
    def getInstance(cls):
        if cls.__singleton_instance == None:
            with cls.__singleton_lock:
                #double check
                if cls.__singleton_instance == None:
                    #simulate ctor delay
                    time.sleep(random.random())
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

class SolutionUnSafe:
    __singleton_instance = None
    @classmethod
    def getInstance(cls):
        if cls.__singleton_instance == None:
            #simulate ctor delay
            time.sleep(random.random())
            cls.__singleton_instance = cls()
        return cls.__singleton_instance
        
def main():
    print_lock = threading.Lock()
    def print_with_lock(message):
        with print_lock:
            print message
            print "-" * 100

    def test_singleton(cls):
        instance = cls.getInstance()
        message = "".join(["Thread id: ",threading.current_thread().getName()," instance id: ",str(instance)])
        print_with_lock(message)

    print "使用threading提供的简单线程进行多线程测试"
    number = raw_input("请输入线程的数量:\n")
    number = int(number)
    print "测试线程安全的单例实现"
    threads = []
    for i in range(0,number):
        t = threading.Thread(target=test_singleton, name=str(i), args=(Solution,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "测试线程不安全的单例实现"
    threads = []
    for i in range(0,number):
        t = threading.Thread(target=test_singleton, name=str(i), args=(SolutionUnSafe,))
        t.start()

if __name__ == '__main__':
    main()
