# import smtplib
#
# my_email = "bavevna@gmail.com"
# password = "qtsojmaumwodjeeu"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="jhon.jhn.sn.90@gmail.com",
#         msg='Subject:Hello\n\nThis is the body of my email.'
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2023:
    print("Yes!")
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1996, month=4, day=6, hour=4)
print(date_of_birth)


