import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email, height, average_height, count):
    from_email = "habeebaramide94@gmail.com"
    from_password = "jgsavfocxbjluaco"
    to_email = email

    subject = "height data"
    message = "Hey there, your height is <strong>%s</strong>.The Average height of all heights received is %s based on <strong>%s</strong> users." % (height, average_height, count)

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

