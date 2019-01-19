import socket
import cv2
import multiprocessing
import pickle
import time
#This part of the code is used to connect to the server side and send the arra in string format using UTF-8 encoding
def send_video_as_string(sock,frame):
    video_string=pickle.dumps(frame)
    try:
        sock.send(video_string.encode('utf-8'))
    except:
        print("Error occured")
def main():
    start=time.time()
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip_address="localhost"
    port=5000
    c=sock.connect((ip_address,port))    
    video=cv2.VideoCapture(0)   #This is the opencv ojject instantization
    while True:
        check,frame=video.read()
        send_video_as_string(c,frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break   
    video.release()
    cv2.destroyAllWindows
    print(video_string)
main()


