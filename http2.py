import socket

"""
在 Python3 里面
str 和 bytes 是两种数据类型

str.encode(编码) 可以得到 bytes
bytes.decode(编码) 可以得到 str

"""

def index():
    html = '''HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
    <h1>Hello World</h1>
    <img src="/doge.gif"/>
    '''
    return html.encode('utf-8')


def image():
    # r 是 read 表示读取
    # b 是 binary 表示处理二进制数据
    # rb 就是 读取二进制
    with open('doge.gif', 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img


def response_for_path(path):
    r = {
        '/': index(),
        '/doge.gif': image(),
    }
    page404 = b'HTTP/1.1 404 NOT FOUNT\r\n\r\n<h1>NOT FOUND</h1>'
    return r.get(path, page404)


host = ''
port = 3000

s = socket.socket()
s.bind((host, port))


while True:
    s.listen(5)
    connection, address = s.accept()
    request = connection.recv(1024)
    request = request.decode('utf-8')
    path = request.split()[1]
    # GET /gua HTTP/1.1
    print('ip and request\n{}'.format(request))

    response = response_for_path(path)

    print('response, ', path, response)
    connection.sendall(response)

    connection.close()
