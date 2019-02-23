import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#Loading Image 

img =cv2.imread('coins.jpg')
img_org = img.copy()
img = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
plt.rcParams["figure.figsize"] = (16,9)
plt.imshow(img,cmap='gray')
#plt.show()
#Applying Blur to the image

img = cv2.GaussianBlur(img, (21,21), cv2.BORDER_DEFAULT)
plt.rcParams["figure.figsize"] = (16,9)
plt.imshow(img,cmap='gray')
#plt.show()

all_circs = cv2.HoughCircles(img , cv2.HOUGH_GRADIENT,0.9,500,param1 = 20 , param2 = 30,minRadius=100 , maxRadius=500 )
all_circs_rounded = np.uint16(np.around(all_circs))

print(all_circs_rounded)
print(all_circs_rounded.shape)
print('I have found ' + str(all_circs_rounded.shape[1]) + ' coins')


count =1
for i in all_circs_rounded[0,:]:
    cv2.circle(img_org,(i[0],i[1]),i[2],(50,200,200),5)
    cv2.circle(img_org,(i[0],i[1]),2,(255,0,0),3)
    cv2.putText(img_org, "Coin "+ str(count),(i[0]-70,i[1]+30),cv2.FONT_HERSHEY_SIMPLEX,1.1,(255,0,0),2)
    count +=1

plt.rcParams["figure.figsize"] = (16,9)
plt.imshow(img_org)
plt.show()