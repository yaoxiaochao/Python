import request

proxies = {
	'http': 'socks5://User:Pwd@host:port'
	'htts': 'socks5://User:Pwd@host:port'
}

s = requests.get('http://2018.ip138.com/ic.asp', proxies=proxies)
page = s.text

ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',page)

from twilio.rest import Client

# 下面认证信息的值在你的 twilio 账户里可以找到
account_sid = "ACcb71f0a88cb94a1fdcb04dcdc859ce5b"
auth_token = "e0658a6ca2b6b8126e5d55e0b43785f7"
client = Client(account_sid, auth_token)

message = client.messages.create(to="",  # 区号+你的手机号码
                                 from_="+12017333824",  # 你的 twilio 电话号码
                                 body=ip)

print(message.sid)