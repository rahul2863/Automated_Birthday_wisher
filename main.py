##################### Extra Hard Starting Project ######################
import random

# 1. Update the birthdays.csv
import pandas as pd
import datetime as dt
import os
import smtplib

data = pd.read_csv("birthdays.csv")
df = pd.DataFrame(data)


# 2. Check if today matches a birthday in the birthdays.csv

today = (dt.datetime.now().month, dt.datetime.now().day)
print(today)
num_of_rows = df.shape[0]
print(num_of_rows)
for i in range(num_of_rows):
    if (df.loc[i, "month"], df.loc[i, "day"]) == today:
        # Specify the directory
        directory = './letter_templates'
        # Get a list of all files in the directory
        all_files = os.listdir(directory)

        print(all_files)
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_file = random.choice(all_files)
        print(random_file)

        with open(f"letter_templates/{random_file}", "r") as fp:
            content = fp.read()
        updated_wishes = content.replace("[NAME]", df.loc[i, "name"])
        print(updated_wishes)

        # 4. Send the letter generated in step 3 to that person's email address.
        email = "rahul.rs2863@gmail.com"
        password = "pspi ryqe uiuq rwyf"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=df.loc[0, "email"],
                msg=f"Subject: Happy Birthday!\n\n{updated_wishes}"
            )






