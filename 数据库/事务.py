"""
事务 是指一系列sql操作的集合 要么成功 要么失败回滚
事务具有四个特性
Atomicity 原子性： 作为一个整体存在，要么全部执行，要么全部失败
Consistency 一致性： 数据完整性没有被破坏，就是数据库从一个一致性状态转换到另一个一致性状态
Isolation 隔离性： 多个事务并发执行时，互不影响
Durability 持久性：一个事务提交，对数据库的修改永远保留
"""

"""
事务隔离级别
1.读未提交
	读到别的事务未提交的数据，脏读
2.读已提交
	只能读取到已提交的事务，解决了脏读问题，但是不可重复读
3.可重复读（mysql默认隔离级别）
	在一个事务内多次读取数据是一致的。解决了脏读和不可重复读问题，但是会出现幻读
4.串行化
	最高隔离级别，事务串行化执行，一个一个排队，解决了脏读、幻读、不可重复读问题，但是效率很低
"""