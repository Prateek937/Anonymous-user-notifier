import cv2
import numpy as np
import time

'''
There are many pretrained models which can detect the faces. One of the model is given below.
Download this CascadeClassifier using command: 
$ wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

(OR)

Go to the link :-
https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
'''

# Loading the classifier/Model
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Function for cropping images
def faceCropper(image):
    # Converting the image to gray Scale for ease and accuracy in model training
    grayScaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecting the faces
    # It will give the coordinates of the face
    faces = model.detectMultiScale(grayScaled,1.3, 5)
    if faces == ():
        return len(faces), None
    else:
        for (x1, y1, x2, y2) in faces:
            croppedFace = grayScaled[y1:y1+y2, x1:x1+x2]
            return len(faces), croppedFace

# Function for clicing images
def imageClicker(dest, capture, count):
    status, image = capture.read()
    cv2.imshow("Cheeze!", image)
    numberOfFaces, cropped = faceCropper(image)
    if cropped is None:
        print("No face detected...[Skipped]")
    elif numberOfFaces == 2:
        print("Two faces detected...[Skipped]")
    else:
        # Resize the image    
        face = cv2.resize(cropped, (200, 200))
    
        # Save the images to the path
        destination = dest + str(count) + '.jpg'
        cv2.imwrite(destination, face)
        print("{} saved".format(destination), end='\r')
        time.sleep(0.1)

def initiateClick(dest):
    numberOfImages = int(input("Enter the number of images you want to click: "))
    print("PRESS ENTER TO INITIATE...", end = "")
    input()
    capture = cv2.VideoCapture(0)
    for count in range(int(numberOfImages)):
        imageClicker(dest, capture, count)
        if cv2.waitKey(1) == 13 or count == numberOfImages-1:
            print("{} photos were clicked and saved to ./data/".format(numberOfImages))
            break

    cv2.destroyAllWindows()
    capture.release()

