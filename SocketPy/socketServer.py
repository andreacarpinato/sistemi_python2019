import socket 

host='127.0.0.1'
port = 65432
#ipv4 AF_INET
#protocollo tcp SOCK_STREAM 

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn,addr=s.accept()
    with conn:
        print('connesso con ',addr)
        data=conn.recv(4096)
        conn.sendall(data)


