import socket
import pickle
import cv2
def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',5000))
    sock.listen(5)
    conn,addr=sock.accept()
    while True:
        data=conn.recv(5096)
        if data!=None:
            frame=pickle.loads(data)
            cv2.imshow(frame)
        if cv2.waitkey==ord('q'):
            conn.close()
            break
main()
