import socket, cv2, pickle, struct
server_socket =socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host_name =socket.gethostname()
host_ip =socket.gethostbyname (host_name)
print("HOST IP:",host_ip) 
print("\t\t\t\n===============================================")

print("Socket Created")

print("\t\t\t\n===============================================")

server_socket.bind(('192.168.43.87',9999))

print("Socket Bind Successfully") 

print("\t\t\t\n===============================================")
server_socket.listen (5)

print("LISTENING AT:")

print("\t\t\t\n===============================================")

print("Socket Accept")

while True:
    client_socket, addr =server_socket.accept() 
    print('GOT CONNECTION FROM:' , addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while(vid. isOpened()):
            img, frame =vid.read()
            a =pickle.dumps(frame)
            message =struct.pack("Q", len(a))+a
            client_socket.sendall(message)
            cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key==13:
                client_socket.close()
