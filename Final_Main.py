
import amino
from gtts import gTTS
import time
import requests
from uuid import uuid4
client=amino.Client()
print("\t\033[1;32m Alexa1.0  \033[1;36m Community Bot \n\n")
email="kaifsahil1111@gmail.com"
password="kaifsahil+++"

client.login(email=email,password=password)

cid="188229182"
cidy=188229182

adm=[]
##admx=["http://aminoapps.com/p/link1","http://aminosapps.com/p/link2"]
self=client.socket
def generate_transaction_id(self):
        return str(uuid4())
transaction=generate_transaction_id(self)

admx=["http://aminoapps.com/u/the_kaif_shl_m_0_2"]

for i in admx:
	try:
		w=client.get_from_code(i).objectId
		adm.append(w)
	except:
		print("invalid admin links/format")
subclient=amino.SubClient(comId=cid,profile=client.profile)

print("inside community")


msg="""♡    ∩_∩
 （„• ֊ •„)♡
 ┏━━∪∪━━━ღ❦ღ━━┓

[BC]❀❀✿✿❀❀✿✿❀❀✿✿❀❀
 ᕼOᒪᗩ ✿
[C]༄ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʜᴀᴛ
[C]༄ʀᴇᴀᴅ ᴀɴᴅ ғᴏʟʟᴏᴡ ᴛʜᴇ ɢᴄ ʀᴜʟᴇs
[C]༄ᴀɴᴅ ᴇɴᴊᴏʏ ʏᴏᴜʀ sᴛᴀʏ ʜᴇʀᴇ 
[C]༄ᴀɴᴅ ᴍᴀᴋᴇ ɴᴇᴡ ғʀɪᴇɴᴅs 

[BC]❀❀✿✿❀❀✿✿❀❀✿✿❀❀

                        ┗ღ❦ღ━━━━━━━━┛
                                            ヽ(‧ω‧`)ﾉ
                                                 |    |
                                                 UU"""
print("Bot joined community")
subclient=amino.SubClient(comId=cid,profile=client.profile)  				
print("Joined all chatrooms")
print("Alexa 1.0 Ready")
l=[]
lis = ["It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful","yes","No" ,"Probably","100%", "Not sure"]

@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""
[c]Welcome <${data.message.author.nickname}$>
{msg}""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
				
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	if data.comId==cidy:
		try:
			subclient.send_message(chatId=data.message.chatId,message="""[BC]━❃❃❃┅━Rip━┅❃❃❃━
[C]「 OH NOO !! 」
[C]Someone has left 💀 the
[C]group chat.
[BC]━❃❃❃┅━Rip━┅❃❃❃━""")
			print(f"Someone left the gc")
		except Exception as e:
			print(e)

@client.event("on_text_message")
def on_text_message(data):
	if data.comId==cidy:
		ex=data.message.content
		cd=ex.split(' ')
		x=cd[0]
		c=cd[1:]
		adx=[]
		for w in cd:
			adx.append(w)
		print(adx)
		if ex:
			for i in adx:
				if len(i)<=50:
					if i[:23]=="http://aminoapps.com/p/" or i[:23]=="http://aminoapps.com/c/":
						fok=client.get_from_code(i)
						cidx=fok.path[1:fok.path.index("/")]
						if cidx!=cid:
							try:
								subclient.delete_message(chatId=data.message.chatId,messageId=data.message.messageId,asStaff=True)
								s=subclient.get_chat_thread(data.message.chatId).title
								subclient.start_chat(userId=adm,message=f"ndc://x{cid}/user/profile/{data.message.author.userId} was advertisng in {s}")
								
								subclient.send_message(chatId=data.message.chatId,message=f"<${data.message.author.nickname} don't advertise here")
								print("spotted advertiser")
							except Exception as e:
								print(e)
			if x.lower()=="!llock" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Locked commands {l}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!lock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.append(i)
							subclient.send_message(chatId=data.message.chatId,message=f"locked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to admin")
					except Exception as e:
						print(e)
			if x.lower()=="!unlock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.remove(i)
							subclient.send_message(chatId=data.message.chatId,message=f"Unlocked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to admin")
					except Exception as e:
						print(e)
			if x.lower()=="!vc" and c==[]:
				try:
					subclient.invite_to_vc(userId=data.message.author.userId,chatId=data.message.chatId)
					print(f"Invited {data.message.author.nickname} to vc")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co/host/host/staff id to invite u to vc, <$@{data.message.author.nickname}$>")
			if x.lower()=="!inviteall" and c==[]:
				if x.lower() not in l:
					try:
						h=subclient.get_all_users(start=0,size=1000).profile.userId
						m=len(h)
						for u in h:
							try:
								subclient.invite_to_chat(userId=u,chatId=data.message.chatId)
							except Exception as e:
								print(e)
								pass
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]Invited {m} users in GC")
						print(f"invited {data.message.author.nickname} to vc")
					except Exception as e:
						print(e)
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co/host/host/staff id to invite u to vc, <$@{data.message.author.nickname}$>")
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Inviteall command is locked")
					except:
						pass
			if x.lower()=="!pm" and c==[]:
				if x.lower() not in l:
					try:
						subclient.start_chat(userId=data.message.author.userId,message="Hey DJ here !")
						subclient.send_message(chatId=data.message.chatId,message=f"Check your pm <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
						print(f"invite {data.message.author.nickname} to pm")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Pm command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="!onlinemem" and c==[]:
				if x.lower() not in l:
					try:
						o=""
						q=subclient.get_online_users(start=0,size=1000)
						for uid in q.profile.nickname:
							o=o+uid+"\n"
						subclient.send_message(chatId=data.message.chatId,message=f"""[c]Online Members
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
						print("done")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Members command is locked")
					except:
						pass

			if x.lower()=="!goodmorning" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[cb]Good morning <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!follow" and c==[]:
				try:
					subclient.follow(userId=data.message.author.userId)
					subclient.send_message(chatId=data.message.chatId,message=f"[c]I started following <${data.message.author.nickname}$> ",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!goodevening" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[cb] Good Evening <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!dance" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
(_＼ヽ
　 ＼＼ .Λ＿Λ.
　　 ＼(　ˇωˇ)　
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ ) 　 Lﾉ
(_／""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!extra" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Extra Commands
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
➼pm                         ➼onlinemem
➼goodmorning       ➼dance
➼goodnight            ➼meme
➼playlist                 ➼inviteall
➼play                       ➼goodnight
➼chocolate            ➼dance
➼8bal
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!prank":
				try:
					for i in c:
						d=int(i)
						print(transaction)
						subclient.send_coins(coins=d, chatId=data.message.chatId, transactionId=transaction)
						subclient.send_message(chatId=data.message.chatId,message=f"Sent {d} coins to Host")
				except Exception as e:
					print(e)
			if x.lower()=="!goodnight" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[cb]Good night <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!botname":
				try:
					t=''
					for i in c:
						t=t+i
						subclient.edit_profile(nickname=t)
						subclient.send_message(chatId=data.message.chatId,message=f"My name changed to {i}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!pico" and c==[]:
				try:
					info = subclient.get_message_info(chatId = data.message.chatId, messageId = data.message.messageId)
					reply_message = info.json['extensions']
					if reply_message:
						image = info.json['extensions']['replyMessage']['mediaValue']
						filename = image.split("/")[-1]
						filetype = image.split(".")[-1]
						urllib.request.urlretrieve(image, filename)
						with open(filename, 'rb') as fp:
							for i in range(1,8):
								try:
									subclient.edit_profile(icon=fp)
								except Exception as e:
									subclient.send_message(data.message.chatId, message="Profile pic changed",replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!playlist" and c==[]:
				try:
					files=os.listdir("music")
					o=""
					for f in files:
						o=o+f+"\n"
					subclient.send_message(chatId=data.message.chatId,message=f"""
[c]Music Playlist
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!8ball":
				try:
					subclient.send_message(chatId=data.message.chatId,message=str(random.choice(lis)),replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!play":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					mx=random.choice(os.listdir("music"))
					if x.lower() not in l:
						sounds=f"music/{mx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="command works only in pm, type /pm to make Alexa join pm")
					except:
						pass
			if x.lower()=="!meme":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					hx=random.choice(os.listdir("memes"))
					if x.lower() not in l:
						sounds=f"memes/{hx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="image")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message=" command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="command works only in pm, type !pm to make DJ join pm")
					except:
						pass
			if x.lower()=="/leader" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Go and check yourself")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="!chocolate" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
╔╦╦
╠╬╬╬╣
╠╬╬╬╣ I ♥
╠╬╬╬╣ Chocolate
╚╩╩╩╝""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			
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
