import random
import smtplib
from datetime import datetime

DAY = 0
my_email = "bavevna@gmail.com"
password = "qtsojmaumwodjeeu"

if datetime.now() == DAY:
    with open('quotes.txt') as file:
        quotes = [line for line in file.readlines()]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jhon.jhn.sn.90@gmail.com",
            msg=f'Subject:Monday quote\n\n{random.choice(quotes)}'
        )
