import birthdayList
import smtplib
import datetime

#Main

flag = False
pswdFlag = True
now = datetime.datetime.now()
email = "" #change this string to your email address (this program requires some extra privacy setting to be set in order to work with Gmail)

emails = []
names = []
age = []

for entry in birthdayList.birthdayList:
    if entry["date"][0] == now.day and entry["date"][1] == now.month:
        emails.append(entry["email"])
        names.append(entry["name"])
        age.append(now.year - entry["date"][2])
        flag = True

if flag:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    while pswdFlag:
        try:
            print("Enter password")
            password = input()
            smtpObj.login(email, password)
            counter = 0
            for emailAdress in emails:
                if emailAdress == "@gmail.com":
                    print("No email given")
                    continue
                message = """Subject: Happy Birthday %s!\n
I wish you Happy birthday from the bottom of my heart! Happy %s!

                            Your Dear Friend.
                """ % (names[counter], str(age[counter]))
                smtpObj.sendmail(email, emailAdress, message)
                print("Email sent to " + emailAdress)
                counter += 1
                pswdFlag = False
        except smtplib.SMTPException:
            pswdFlag = True
            print('Error: Wrong password!')
else:
    print("No one has their birthday today!")


