#read a video stream from a camera(frame by frame)
import cv2

cp=cv2.VideoCapture(0) # 0 means default webcam

while True:
    ret,frame=cp.read()
    
    if(ret==False):
        # is some error occurs
        continue
    
    cv2.imshow("video frame",frame)
    
    key_pressed=cv2.waitKey(1) & 0XFF  # we are doing & because waitkey gives 32 bit output but keyboard keys ascii are in 8 bit
    if(key_pressed==ord('q')):
       # setting key q to break the loop
           break;
       
       
cp.release()
cv2.destroyAllWindows
    