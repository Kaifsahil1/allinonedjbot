import amino
import time
import requests

client=amino.Client()
email="kaifsahil1111@gmail.com"
password="kaifsahil111@@@"
client.login(email=email,password=password)

print("logged in")

n="http://aminoapps.com/c/Indianfamily2"
fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]
print(cid)
subclient=amino.SubClient(comId=cid,profile=client.profile)

print("Joined community")
   			
@client.event("on_group_member_join")
def on_group_member_join(data):
	while True:
			subclient.send_message(chatId=data.message.chatId,message="welcome to chutiyo ka world aye or gaand maraye ",messageType=108)
			print(f"Join spam started")
				
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	while True:
			subclient.send_message(chatId=data.message.chatId,message="vampii ki gaand mai unglii krke jaye",messageType=108)
			print(f"Leave spam started")
			
@client.event("on_text_message")
def on_text_message(data):
	while True:
			subclient.send_message(chatId=data.message.chatId,message="maassage kroge to gandi banjauge",messageType=108)
			print(f"Text spam started")

@client.event("on_sticker_message")
def on_sticker_message(data):
	while True:
			subclient.send_message(chatId=data.message.chatId,message="bahan ka lodu vampii chakka",messageType=108)
			print(f"Sticker spam started")
			
@client.event("on_image_message")
def on_image_message(data):
	while True:
			subclient.send_message(chatId=data.message.chatId,message="vampii ki gaand maro maje lo free free free if2 walo ki maroo free free free",messageType=108)
			print(f"Image spam started")

print("Spam Bot started")			
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()			