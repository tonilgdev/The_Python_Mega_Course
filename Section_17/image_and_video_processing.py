# Loading, Displaying, Resizing and Creating Images.

import cv2

img = cv2.imread("galaxy.jpg", 0) # 1 color image, 0 greycolor

print(type(img))

print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resixed.jpg",resized_image)
cv2.waitKey(0) # 0 any button, time=2000 ms
cv2.destroyAllWindows()

# Detecting Faces in Images

# import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1,minNeighbors=5)

for x,y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)


print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows

# Capturing Video with Python

# import cv2
import time as t

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # t.sleep(3)
    cv2.imshow("CApturing", gray)
    key = cv2.waitKey(1)

    if key==ord('q'):
        break
    
video.release()
cv2.destroyAllWindows