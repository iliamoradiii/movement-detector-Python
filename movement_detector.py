import cv2

Cap=cv2.VideoCapture(0)

_,frame1=Cap.read()
_,frame2=Cap.read()

while(Cap.isOpened()):
    # اختلاف دوتا عکس 
    diff=cv2.absdiff(frame1,frame2)
    # سیاه سفید 
    Gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    #نویز گیری
    Blured=cv2.GaussianBlur(Gray,(5,5),0)
    #آستانه 
    _,Thresh=cv2.threshold(Blured,20,255,cv2.THRESH_BINARY)
    #افزایش مقدار 
    Dilated=cv2.dilate(Thresh,None,iterations=5)
 
    ### پیدا کردن کانتور
    contours, _ =cv2.findContours(Dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        #مساحت کمتر از حد مطلوب
        if(cv2.contourArea(contour)<10000):
            pass
        else:
            frame1=cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(frame1,"Status:{}".format("Movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    
    cv2.imshow("video",frame1)
    frame1=frame2
    _,frame2=Cap.read()


    if(cv2.waitKey(40)==27):
        break

Cap.release()
cv2.destroyAllWindows()
