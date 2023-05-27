##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import random
import smtplib
from datetime import datetime

import pandas

my_email = "bavevna@gmail.com"
password = "qtsojmaumwodjeeu"


birthdays = pandas.read_csv("birthdays.csv")
dict_birthdays = birthdays.to_dict(orient="records")
for birthday in dict_birthdays:
    date = datetime(year=datetime.today().year, month=birthday['month'], day=birthday['day']).date()
    if date == datetime.today().date():
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter_text = letter.read()
            new_letter = letter_text.replace("[NAME]", birthday['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday['email'],
                msg=f'Subject:Happy Birthday!\n\n{new_letter}'
            )
