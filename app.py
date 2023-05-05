from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/samson')
def samson():
    return render_template('samson.html')

@app.route('/marco')
def marco():
    return render_template('marco.html')

@app.route("/sendemail/", methods=['POST'])
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        your_name = "IP Siu Fung Ernest"
        your_email = "wongkamming98@gmail.com"
        your_password = "hvrdjxvzzwrozuym"

        # Logging in to our email account
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(your_email, your_password)

        # Sender's and Receiver's email address
        sender_email = "wongkamming98@gmail.com"
        receiver_email = "210123688@stu.vtc.edu.hk"

        msg = EmailMessage()
        msg.set_content("First Name : "+str(name)+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage : "+str(message))
        msg['Subject'] = 'New Response on Personal Website'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
        except:
            pass
    return redirect('/');

if __name__ == "__main__":
    app.run(debug=True)
