#read a video stream from a camera(frame by frame)
import cv2

cp=cv2.VideoCapture(0) # 0 means default webcam
faceclassifier=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
                                     
while True:
    ret,frame=cp.read()
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                                     
    if(ret==False):
        # is some error occurs
        continue
    faces=faceclassifier.detectMultiScale(grayframe,1.3,5)                               
    
                                     
    for x,y,w,h in faces:
                       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("video frame",frame)
    
    key_pressed=cv2.waitKey(1) & 0XFF  
    if(key_pressed==ord('q')):

           break;
       
       
cp.release()
cv2.destroyAllWindows
    