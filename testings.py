import socket

def socketRequest(ip, port):
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.settimeout(5)
        c.connect((ip, int(port)))
        c.send(b"")
        res = c.recv(4096)
        return res.decode("utf-8", errors="replace").replace("\n", "  ")
    except Exception as e:
        pass 
        return None
    
print(socketRequest("172.24.109.7", 5405))