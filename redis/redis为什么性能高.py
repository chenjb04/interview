"""
1.完全基于内存读写，内存读写速度很快
2.单线程模型，避免了线程或者进程切换造成的性能损耗
3.采用IO多路复用模型，复用可以使redis单线程连接多个请求
4.内置的数据结构，优化速度
"""