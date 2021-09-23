import samino,time,os,sys
vip = [""] # userIds
client = samino.Client("22C47F6E327764942738F7636FE42FB247FC9E4629C98C96D91CC1456D25FD07A153995C82213E4AC0")
client.login(email="kaifsahil1111@gmail.com",password="kaifsahil111@@@")

@client.event("on_message")
def on_message(data: samino.lib.Event):
	msg = data.message.content
	msgId = data.message.messageId
	comId = data.ndcId
	chatId = data.message.chatId
	userId = data.message.userId
	nickname = data.message.author.nickname
	try: mentionIds = data.message.json["extensions"]["mentionedArray"]
	except: pass
	local = samino.Local(comId)
	if msg.startswith("*tap"):
		local.send_message(chatId,f"{nickname} done ",asWeb=True)
		for a in range(300): client.watch_ad(userId)

def socketRoot():
	while True:
		print("updating socket....")
		client.launch()
		shundle = client.socket;shundle.close();client.launch()
		time.sleep(300)
		sys.argv;sys.executable;print("restart now")
		os.execv(sys.executable, [ python ] + sys.argv)
socketRoot()