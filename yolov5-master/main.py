import cv2
vidcap = cv2.VideoCapture(0)
 
count = 0
 
while(vidcap.isOpened()):
    ret, image = vidcap.read()
 
    if(int(vidcap.get(1)) % 10 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("./img/cat_%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1
    cv2.waitKey()
    

vidcap.release()