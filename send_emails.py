import smtplib

my_email = "your_email@gmail.com"
password = "your_password"

with smtplib.SMTP("smtp.gmail.com") as connect:
  connect.starttls()
  connect.login(user=my_email, password=password)
  connect.sendmail(
    from_addr=my_email, 
    to_addrs="someone_email@yahoo.com", 
    msg="Subject:Hello\n\nThis is the body of the email.")
  
