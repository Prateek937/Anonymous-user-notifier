import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import subprocess as sb
import time

# This function will return the training and labels
def trainAndlabelsData(images, sourcePath):
    trainingData, labels, l = [], [], 0
    # # Iterate through the image list
    for image in images:
        source = sourcePath + image
        # Read the image
        image = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
        # Append the image to the training dataset 
        # Append the label too 
        trainingData.append(np.asarray(image, dtype=np.uint8))
        labels.append(l)
        l += 1
    
    return trainingData, labels

def train(sourcePath):
    imageFiles = listdir(sourcePath)

    # Creating dataset with labels for training
    print("Fetching Clicked Images...")
    trainingData, labels = trainAndlabelsData(imageFiles, sourcePath)

    '''
    - Create a model for face recognition
    - For getting the face recognition models you need to install opencv-contrin-python
    - Use the below command to install it
        # pip install opencv-contrib-python
    NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()
    '''
    print("Creating Face Recognition model...")
    faceRecognizer  = cv2.face_LBPHFaceRecognizer.create()

    # Train the model
    print("Intiating training of model...")
    error = faceRecognizer.train(np.asarray(trainingData), np.asarray(labels, dtype='int32'))

    print("Training successful!")

    return faceRecognizer
