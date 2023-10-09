import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

from twilio.rest import Client
import requests

# Set up your email parameters
sender_email = "lalitdeore12@gmail.com"
sender_password = "khdehitpllwhhkxk"
receiver_email = "lalitdeore00@gmail.com"
subject = " Gun Detected"
body = "A gun was detected in the following image:"

# Find the latest saved image in the directory
image_directory = "D:\\mp\\mp\\Client_Side\\saved_frame"  

latest_image = max([os.path.join(image_directory, f) for f in os.listdir(image_directory)], key=os.path.getctime)

# Create a message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body))

# Attach the image to the message
with open(latest_image, 'rb') as f:
    img_data = f.read()
    image = MIMEImage(img_data, name=os.path.basename(latest_image))
    msg.attach(image)

# Send the message
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)

print("Email sent!")



# Your Twilio account SID and auth token
account_sid = 'AC0906b645c9a7529cde6b6d09bdbdf3f2'
auth_token = '9cc5006e67267a79a9deb8cb0c73b448'

# Create a Twilio client
client = Client(account_sid, auth_token)

# The phone numbers
from_phone_number = '+16206858405'  # Your Twilio phone number
to_phone_number = '+919860073134'  # The recipient's phone number

# Local path of the image file
image_path = 'D:\\mp\\mp\\Client_Side\\saved_frame\\frame.jpg'  # Replace with the actual local path of the image

# Upload the image to an online storage platform (e.g., Imgur)
image_url = 'https://api.imgur.com/3/upload'
headers = {'Authorization': 'Client-ID YOUR_CLIENT_ID'}
image_data = {'image': open(image_path, 'rb')}
response = requests.post(image_url, headers=headers, files=image_data)
media_url = response.json()['data']['link']

# The message content
message_body = 'ALERT: A gun has been detected in the bank!'

# Send the message with the image attachment
message = client.messages.create(
    body=message_body,
    media_url=[media_url],  # List of media URLs (in this case, only one image)
    from_=from_phone_number,
    to=to_phone_number
)

print('Message sent with image attachment!')


