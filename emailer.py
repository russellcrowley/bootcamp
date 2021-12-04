# email function using yagmail
import yagmail
# you need to setup your email account (after importing yagmail) with yagmail.register('mygmailusername', 'mygmailpassword')
# see https://yagmail.readthedocs.io/en/latest/setup.html for more details

def emailer(subject, contents, to="XXX"):
    """ simple script to send an email. Replace XXX with your target email and the account the email is sending from """
    # simple email sender using yagmail
    yag = yagmail.SMTP("XXX")
    contents = contents
    yag.send(to, subject, contents)
    return

if __name__ == "__main__":
    emailer()