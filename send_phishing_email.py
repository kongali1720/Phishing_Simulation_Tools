#!/usr/bin/env python3
"""
send_phishing_email.py
Phishing Email Simulator for Cybersecurity Awareness
By Kongali1720
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(smtp_server, port, sender_email, sender_password, receiver_email):
    # Buat pesan email phishing simulasi
    message = MIMEMultipart("alternative")
    message["Subject"] = "Important: Verify Your Account Now!"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Email HTML (dummy phishing content)
    html = """
    <html>
    <body>
        <h2 style="color:red;">Action Required!</h2>
        <p>Your account has suspicious activity. Please <a href="http://localhost/phishing_page/index.html" target="_blank">click here to verify your account</a> immediately.</p>
        <p><i>This is a phishing simulation for awareness purpose only.</i></p>
    </body>
    </html>
    """

    # Email plain text fallback
    text = """\
    Action Required!

    Your account has suspicious activity.
    Please visit the following link to verify your account:
    http://localhost/phishing_page/index.html

    This is a phishing simulation for awareness purpose only.
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()

    print(f"Connecting to SMTP server {smtp_server}:{port}...")
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            print(f"Logged in as {sender_email}")
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"Phishing simulation email sent to {receiver_email}!")
    except Exception as e:
        print("Error sending email:", e)

def main():
    print("=== Phishing Email Simulator ===")

    smtp_server = input("SMTP Server (e.g. smtp.gmail.com): ").strip()
    port = int(input("SMTP Port (465 for SSL): ").strip())
    sender_email = input("Sender Email: ").strip()
    sender_password = input("Sender Email Password (or App Password): ").strip()
    receiver_email = input("Receiver Email (target): ").strip()

    send_phishing_email(smtp_server, port, sender_email, sender_password, receiver_email)

if __name__ == "__main__":
    main()
