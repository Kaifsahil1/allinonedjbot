import AminoLab
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_GREEN_SEA + style.BOLD)
print("""𝗗𝗝 𝗦𝗔𝗛𝗜𝗟""")
print(pyfiglet.figlet_format("Aminospam1.0", font="eftitalic"))
client = AminoLab.Client()
email ="kaifsahil1111@gmail.com"
password = "kaifsahil111@@@"
client.auth(email=email, password=password)
msg = "check"
msgtype = "108"
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
ndcId = clients.ndcId[int("1")-1]
chats = client.my_chat_threads(ndcId=ndcId, size=100)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
threadId = chats.threadId[int("1")-1]
while True:
	print("Spamming...")
	with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
		_ = [executor.submit(client.send_message, ndcId, threadId, msg, msgtype) for _ in range(100)]