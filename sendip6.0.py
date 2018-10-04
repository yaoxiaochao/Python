import smtplib
import os
import time
import requests
import re



def find_ip():
    try:
        p = requests.get('http://2018.ip138.com/ic.asp')
        page = p.text
        ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', page)
        return ip
    except UnicodeDecodeError as e:

        print(e)

    except urllib.error.HTTPError as e:

        print(e)

    except urllib.error.URLError as e:

        print(e)

    except socket.timeout as e:

        print(e)

    except http.client.RemoteDisconnected as e:

        print(e)

    except ConnectionResetError as e:

        print(e)


def send_email(self):
    FROMADDR = "***@163.com"
    LOGIN    = FROMADDR
    PASSWORD = "***"
    TOADDRS  = ["***@gmail.com" ,"***@gmail.com"]
    SUBJECT  = "Updated for public ip of office network"

    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
           % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
    msg += "Please check below ip.\r\n " +str(self)

    server = smtplib.SMTP('smtp.163.com', 25)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    server.sendmail(FROMADDR, TOADDRS, msg)
    server.quit()


def run(n):
    while True:
        ip = find_ip()
        time.sleep(n)
        ip1 = find_ip()
        status = os.system('ping -c 1 www.baidu.com')
        if ip != ip1 and ip1 != [] and status == 0:
            send_email()
        else:
            print("no internet")


if __name__ == '__main__':
    run(10)
