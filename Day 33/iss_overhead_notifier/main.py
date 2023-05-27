import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LAT_MIN = MY_LAT - 5.0
MY_LAT_MAX = MY_LAT + 5.0
MY_LONG = -0.127758  # Your longitude
MY_LONG_MIN = MY_LONG - 5.0
MY_LONG_MAX = MY_LONG + 5.0
MY_EMAIL = "bavevna@gmail.com"
PASSWORD = "qtsojmaumwodjeeu"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT_MIN < iss_latitude < MY_LAT_MAX and MY_LONG_MIN < iss_longitude < MY_LONG_MAX:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True


def notify_me():
    print('Send!')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jhon.jhn.sn.90@gmail.com",
            msg='Subject:ISS ALERT\n\nLook up!'
        )


while True:
    if is_iss_overhead() and is_night():
        notify_me()
        time.sleep(60)
