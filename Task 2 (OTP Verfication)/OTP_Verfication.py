import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Generate a random integer between 000000 and 999999
random_number = random.randint(0, 999999)
six_digit_number = f'{random_number:06d}'

# User input for recipient's email address
receiver_email = input("Please Enter Your Email Address: ")

# Email configuration
sender_email = 'test.acc0unt.2069@gmail.com'
subject = 'OTP Verfication'
message = f'The OTP Verfication Code {six_digit_number}'

# SMTP server configuration (for Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

username = 'test.acc0unt.2069@gmail.com'
password = 'gljzmihvivfrqnyg '

# Create a MIMEText object for the email content
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Establish a connection to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption

    # Log in to your email account
    server.login(username, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the connection to the SMTP server
    server.quit()
    print(f'\nEmail sent to {receiver_email} successfully')

except Exception as e:
    print(f'An error occurred: {str(e)}')

while True:
    userOTP = input(f"Please Enter The Recieved OTP on {receiver_email}: ")
    if userOTP == six_digit_number:
        print("Welcome You Are Now Verified :)")
        break
    else:
        print("This OTP Was Incorrect Please Try Again")
