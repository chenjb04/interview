"""
第一次握手： 客户端发送SYN数据包到服务器，进入SYN_SEND状态，等待服务器确认
第二次握手： 服务端收到syn包，必须确认客户的SYN（ack=x+1），同时自己也发送一个SYN包，即SYN+ACK包，进入SYN_RECV状态
第三次握手： 客户端收到服务器的SYN+ACK包，向服务器发送确认包ack=y+1，此包发送完毕，客户端和服务器进入ESTABLISHED状态，完成三次握手


"""