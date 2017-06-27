import socket


# host 为空字符串 是规定 是套路
host = ''
port = 2000

s = socket.socket()
# bind 是服务器用的函数, 用来绑定一个接受连接的端口
s.bind((host, port))


while True:
    # 监听请求, backlog 是三次握手队列中的连接数
    s.listen(5)
    # 如果有请求连接本机, 那么 accept 函数就会返回
    connection, address = s.accept()

    request = connection.recv(1024)

    print('ip and request\n{}'.format(request.decode('utf-8')))

    # 发送bytes给客户端(浏览器)
    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<meta charset="utf-8"><h5>Hello 瓜!</h5>'
    connection.sendall(response.encode('utf-8'))
    connection.close()

