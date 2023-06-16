import smtplib


def send_email(subject, message, from_email, to_emails, username, password):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)

        for to_email in to_emails:
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(from_email, to_email, email_message)

        server.quit()
        return True

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {str(e)}")
        return False
