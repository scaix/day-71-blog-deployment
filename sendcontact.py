import smtplib
import os


def send_contact_data(name, email, phone, msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(os.environ.get('PYTHON_MAIL_ACCOUNT'), os.environ.get('PYTHON_MAIL_PWD'))
        result = connection.sendmail(
            from_addr=email,
            to_addrs=os.environ.get('PYTHON_MAIL_ACCOUNT'),
            msg=f"Subject:new contact {name} (phone: {phone})\n\n{msg}"
        )
        print(result)
