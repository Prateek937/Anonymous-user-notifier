import pywhatkit # For controlling whatsapp with python scripts $pip3 install pywhatkit
from datetime import datetime #datetime module to get current time
from decouple import config # For accessing environment variables

# Funtion for sending whatsapp message
def whatsApp():
    now = datetime.now()           # returns current time
    hr = int(now.strftime("%H"))   # returns Current Hour
    min = int( now.strftime("%M"))  # returns Current mint
    number = config('MOBILE')
    message = "Hello Shilpy! Message from Face Recognizer."

    # Send the message
    pywhatkit.sendwhatmsg(number, message, hr,min+1 ,wait_time=10)

