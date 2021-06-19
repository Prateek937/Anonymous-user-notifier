import cv2 # For using the camera
import os # For running shell commands

# Import other modules
import ImageCollector # For clicking images to train model
import trainModel # Training the model
import mail # Sending mail
import whatsApp # Send a whatsapp message
import awsResource # For launching instances


dataPath = "./data/"
# Click and save images for training the model
ImageCollector.initiateClick(dataPath)

# Train the model
faceRecognizer = trainModel.train(dataPath)

print("Press Enter to start the app..", end="")
input()
capture = cv2.VideoCapture(0)
prateek = 0
anonymous = 0
print("Analyzing...")

while prateek+anonymous <= 100:
    status, image = capture.read()
    cv2.imshow("Analyzing..", image)
    # save the image for future use
    cv2.imwrite(dataPath+"Person.jpg", image)

    # It will take the image, convert to grascale and return the cropped grayscale face  
    numberOfFaces, face = ImageCollector.faceCropper(image)
    if face is None:
        print("No face detected...")

    elif numberOfFaces > 2:
        print("2 faces detected...")
        print("Launching EC2 and 5 EBS Volumes on AWS.")

    else:
        # Predicting whether it is my face or not
        results = faceRecognizer.predict(face)
        
        # Calculating confidence score
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )

        if confidence >= 85:
            prateek += 1
        else:
            anonymous += 1

        if cv2.waitKey(1) == 13:
            break

cv2.destroyAllWindows()
capture.release()

if prateek > anonymous:
    print("Hello Prateek! Nice to see you.")
    print("A mail has been sent to you with you photo as attachment.")
    # Sending mail
    mail.sendEmail(dataPath+"Person.jpg")

    # Sending a whatsapp message to a friend
    print("Sending Whatsapp messaage to you frined...")
    whatsMessage = "Hello Shilpy! Message from Face Recognizer."
    whatsApp.whatsApp(whatsMessage)
else:
    print("Unknown faces detected...")
    print("Launching EC2 Instance with 5 EBS Volumes Attached to it...")
    
    print("Using boto3 in python script...")
    awsResource.launchInfra()

    print("Using terraform Script...")
    os.system("terraform -chdir=./awsTerraform/ init")
    os.system("terraform -chdir=./awsTerraform/ apply -auto-approve")

