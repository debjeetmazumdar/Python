import smtplib  # imported built in library smtplib for sending email


mail_server_connection=smtplib.SMTP(host='smtp.gmail.com',port=587) # establishing instance of connection to gmail server


mail_server_connection.ehlo() # checking connection got establised or not


mail_server_connection.starttls() # starting tls service for encryption on the establised connection


import getpass #importing getpass to enable non-visible text while entering password and email id


# asking user to enter email id and password

email_id = input('Enter your email id: ')
password = getpass.getpass('Enter your password: ') # this password is actually 'app' password and not normal gmail account password


mail_server_connection.login(email_id,password) # making a login attempt to the gmail server via the established connection


#compose the email like we normally do in webpage or app

from_address=email_id
to_address=input("Enter recepient email id")
subject=input("Enter the subject: ")
message=input("Enter the body message: ")
msg="Subject: "+ subject + '\n' + message


mail_server_connection.sendmail(from_address,to_address,msg)


mail_server_connection.quit()




