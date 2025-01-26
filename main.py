# Aim: Break Video into Multiple Images and store in a folder

import cv2

vidcap=cv2.VideoCapture(r'nature.mp4')
ret, image=vidcap.read()

count=0

while True:
    if ret== True:
        cv2.imwrite(r'C:\Users\Vaishnavi\OneDrive\Desktop\pr\cv\\frames\\imgN%d.jpg'%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*100))
        ret,image=vidcap.read()
        cv2.imshow('res', image)

    count+=1
    k=cv2.waitKey(1)
    if k==ord('v'):
        break

vidcap.release()
cv2.destroyAllWindows()
