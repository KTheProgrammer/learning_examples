import smtplib

my_email = "your_email@gmail.com"
password = "your_password"

connect = smtplib.SMTP("smtp.gmail.com")
connect.starttls()
connect.login(user=my_email, password=password)
connect.sendmail(from_addr=my_email, to_addrs="someone_email@yahoo.com", msg="Hello")
connect.close()
