import cv2
import os

my_image = cv2.imread("numbers.jpg")
number=0
count=1
for i in range(0,1000,20):
    for j in range(0,2000,20):
        crop_image=my_image[i:i+20,j:j+20]
        os.makedirs(f"digits/{number}",exist_ok=True)
        cv2.imwrite(f"digits/{number}/number{number}_{count}.jpg",crop_image)
        count+=1

        if count>500:
            number+=1
            count=1