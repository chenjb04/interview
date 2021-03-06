# 迭代器
"""
解释器需要迭代对象x时，会调用iter函数
iter函数作用：
1、检查对象是否实现了__iter__方法，如果实现就会获取一个迭代器
2、如果没有__iter__方法，但是实现了__getitem__方法，会创建一个迭代器，尝试顺序获取
3、如果尝试失败，会抛出typeError
鸭子类型 只要实现了__iter__方法或者实现了__getitem__方法且参数从0开始的int，就认为对象是可迭代的

可迭代对象和迭代器：python从可迭代对象中获取迭代器
标准的迭代器接口实现两个方法 
__next__和__iter__
"""
'-----------------------------------------------------------------------------------'
# 生成器
"""
生成器是一种特殊的迭代器   只要函数中包含yield关键字 就是生成器函数
"""