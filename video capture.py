#convert face colour
##Inspried By Sentdex

#import all the required libaries
import numpy as np
import cv2


#capture by the webcam if you use extrnal thean pass "1"
face= cv2.VideoCapture(0)


while(True):     #start the infinite loop
    ret, frame = face.read()    #if its true then ret is working then its start reading the face
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #convert the face colour into gray
    transparent= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #convert  it into rgb

    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('transparent',transparent)
    if cv2.waitKey(1) & 0xFF == ord('s'):  #wait for s key to press and break the infinite loop
        break


face.release()
cv2.destroyAllWindows()
