import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def tool_email_sender(receiver: str, subject: str, body: str, sender="rohitmudili5@gmail.com", pwd="ivnb ceba anio gqdm") -> str:
    """Sends an email using SMTP
    Args:
        receiver: Recipient's email address
        subject: Email subject line 
        body: Main content of the email
        sender: Sender's email address (default: rohitmudili5@gmail.com)
        pwd: Sender's email password (default: 'ivnb ceba anio gqdm')
    """
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    try:
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(sender, pwd)
            server.sendmail(sender, receiver, message.as_string())
        
        return f"Email sent successfully to {receiver}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    result = tool_email_sender(receiver="rohitmudili5@gmail.com", subject="Test", body="Repair_request has been logged and respective team has been notified") 
    print(result)

if __name__ == "__main__":
    main()
