import smtplib
import ssl


# Set these vars
smtp_server = 'smtp.gmail.com'  # or something else
sender_email = 'sender_email@something.com'
sender_password = 'secret_password'
receiver_email = 'receiver_email@something.com'

port = 587  # for starttls
context = ssl.create_default_context()


def send_email(sender=sender_email, receiver=receiver_email,
               sender_password=sender_password, subject='', text=''):
    message = f'Subject: {subject}\n\n{text}'
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender, sender_password)
        server.sendmail(sender, receiver, message)


def main():
    send_email(subject='Some subject', text='Some text.')


if __name__ == '__main__':
    main()
