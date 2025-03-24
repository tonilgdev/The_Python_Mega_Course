# Exercise: Batch Image Resizing
# Write a script that resizes all images in a directory to 100x100. You can find an attached ZIP file with some image files in the Resources.

import cv2

img1 = cv2.imread("galaxy.jpg", 1) # 1 color image, 0 greycolor
img2 = cv2.imread("kangaroos-rain-australia_71370_990x742.jpg", 1) # 1 color image, 0 greycolor
img3 = cv2.imread("Lighthouse.jpg", 1) # 1 color image, 0 greycolor
img4 = cv2.imread("Moon sinking, sun rising.jpg", 1) # 1 color image, 0 greycolor

resized_image1 = cv2.resize(img1,(100,100))
resized_image2 = cv2.resize(img2,(100,100))
resized_image3 = cv2.resize(img3,(100,100))
resized_image4 = cv2.resize(img4,(100,100))

cv2.imwrite("Galaxy_100.jpg",resized_image1)
cv2.imwrite("kangaroos_100.jpg",resized_image2)
cv2.imwrite("Lighthouse_100.jpg",resized_image3)
cv2.imwrite("Moon_100.jpg",resized_image4)

# Solution (https://docs.python.org/3/library/glob.html)

import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)