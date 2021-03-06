"""
缓存雪崩指的是短时间内大量key失效，请求打到后端
解决：
.在给缓存设置失效时间时加一个随机值，避免集体失效。
双缓存机制，缓存A的失效时间为20分钟，缓存B没有失效时间，从缓存A读取数据，缓存A中没有时，去缓存B中读取数据，并且启动一个异步线程来更新缓存A。
"""