import requests
import re
import time
import smtplib
import os


def find_ip():
    if (os.system('ping -c 1 www.baidu.com') == 0):
        s = requests.Session()
        p = s.get('http://2018.ip138.com/ic.asp')
        page = p.text

        ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', page)
        return ip
        s.close()
    else:
        print("connection failed")

def send_email(self):
    if (os.system('ping -c 1 www.baidu.com') == 0):
        FROMADDR = "xxx@163.com"
        LOGIN = FROMADDR
        PASSWORD = "xxx"
        TOADDRS = ["xxx@gmail.com", "xxx@gmail.com"]
        SUBJECT = "Updated for public ip of office network"

        msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
               % (FROMADDR, ", ".join(TOADDRS), SUBJECT))
        msg += "Please check below ip.\r\n" + str(self)

        server = smtplib.SMTP('smtp.163.com', 25)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(LOGIN, PASSWORD)
        server.sendmail(FROMADDR, TOADDRS, msg)
        server.quit()
    else:
        print("no internet")


def run(n):
    while True:
        ip = find_ip()
        print(ip)
        time.sleep(n)
        ip1 = find_ip()
        print(ip1)
        if ip != ip1:
            send_email(ip1)
        else:
            print("same ip")


if __name__ == "__main__":
    run(100)
