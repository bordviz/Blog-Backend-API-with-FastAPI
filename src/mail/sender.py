from email.message import EmailMessage
import smtplib
from config import EMAIL_SEND, EMAIL_PASS

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

def get_email_template_dashboard(username: str, user_email: str, code: int):
    email = EmailMessage()
    email['Subject'] = 'Код верификации'
    email['From'] = EMAIL_SEND
    email['To'] = user_email

    email.set_content(
        '<div>'
            f'<h1 style="color: black; font-weight: 700; text-align: center;">Здравствуйте, {username}, ваш код верификации:</h1>'
            f'<h1 style="color: black; font-size: x-larger; font-weight: 700; text-align: center;">{code}</h1>'
        '</div>',
        subtype='html'
    )
    return email

def send_email_report_dashboard(username: str, user_email: str, code: int):
    email = get_email_template_dashboard(username, user_email, code)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(EMAIL_SEND, EMAIL_PASS)
        server.send_message(email)