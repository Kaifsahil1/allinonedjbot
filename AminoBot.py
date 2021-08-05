import sys
import os
import txt2pdf
from gtts import gTTS, lang
import time
import sys
import amino
from BotAmino import *
from fancy_text import fancy
from BotAmino import BotAmino
import sys
from gtts import gTTS, lang
import emoji
import urllib.request
import requests
import urllib
import requests
import json
from random import uniform, choice, randint

from pathlib import Path
from google_trans_new import google_translator
import asyncio
import random
import os
from os import path
from random import uniform, choice, randint
import os
import threading
import time
import txt2pdf
import random
import urllib.request
from gtts import gTTS, lang
from time import sleep
from threading import Thread
from json import dumps, load
from random import choice, randint
from pathlib import Path
from contextlib import suppress
from datetime import datetime
from pdf2image import convert_from_path
from youtube_dl import YoutubeDL
from BotAmino import BotAmino, Parameters
from json import dumps, load
from random import choice, randint
from pathlib import Path
from contextlib import suppress
from string import punctuation
from unicodedata import normalize

from pdf2image import convert_from_path
from youtube_dl import YoutubeDL
from BotAmino import *

# Big optimisation thanks to SempreLEGIT#1378 ♥


version = "1.7.4"
print(f"AminoBot version : {version}")

path_eljson1 = f"{path_utilities}/elJson.json"
path_eljson2 = f"{path_utilities}/elJson2.json"

client = BotAmino("kaifsahil1111@gmail.com","kaifsahil111@@@")
client.bio ="☞ͥ͟⋆ͣ͟⋆ͫ★⃝🅳J"
client.spam_message = "Cooldown, please wait before doing a command again..."
def print_exception(exc):
    print(repr(exc))


def join_community(comId: str = None, inv: str = None):
    if inv:
        try:
            client.client.request_join_community(comId=comId, message='Cookie for everyone!!')
            return True
        except Exception as e:
            print_exception(e)
    else:
        try:
            client.client.join_community(comId=comId, invitationId=inv)
            return True
        except Exception as e:
            print_exception(e)
@client.command("check")
def test(data):
    data.subClient.send_message(data.chatId, f"DJ BOT IS ONLINE {data.author}")


@client.command("joinamino")
def join_amino(args):
    invit = None
    if client.taille_commu >= 20:
        args.subClient.send_message(args.chatId, "The bot has joined too many communities!")
        return

    staff = args.subClient.get_staff(args.message)

    if args.authorId not in staff:
        args.subClient.send_message(args.chatId, "You need to be in the community's staff!")
        return

    if not staff:
        args.subClient.send_message(args.chatId, "Wrong amino ID!")
        return

    try:
        test = args.message.strip().split()
        amino_c = test[0]
        invit = test[1]
        invit = invit.replace("http://aminoapps.com/invite/", "")
    except Exception:
        amino_c = args.message
        invit = None

    try:
        val = args.subClient.client.get_from_code(f"http://aminoapps.com/c/{amino_c}")
        comId = val.json["extensions"]["community"]["ndcId"]
    except Exception:
        return

    isJoined = val.json["extensions"]["isCurrentUserJoined"]
    if not isJoined:
        size = val.json['extensions']['community']['membersCount']
        if size < 100:
            args.subClient.send_message(args.chatId, "Your community must have at least 100 members")
            return

        join_community(comId, invit)
        val = client.client.get_from_code(f"http://aminoapps.com/c/{amino_c}")
        isJoined = val.json["extensions"]["isCurrentUserJoined"]
        if isJoined:
            client.add_community(args.message)
            client[comId].run()
            auth = client.get_community(comId).get_user_info(args.message).nickname
            client.get_community(comId).ask_amino_staff(f"Hello! I am a bot and i can do a lot of stuff!\nI've been invited here by {auth}.\nIf you need help, you can do !help.\nEnjoy^^")
            args.subClient.send_message(args.chatId, "Joined!")
            return
        args.subClient.send_message(args.chatId, "Waiting for join!")
        return
    else:
        args.subClient.send_message(args.chatId, "Allready joined!")
        return

    args.subClient.send_message(args.chatId, "Something went wrong!")
@client.command("global")
def g(data):
																		mention=data.subClient.get_message_info(chatId=data.chatId,messageId=data.messageId).mentionUserIds
																		for user in mention:
																			link=client.get_from_id(user,0).shortUrl
																			data.subClient.send_message(data.chatId,message=link)

@client.command("title")
def title(args):
    if client.check(args, 'staff', id_=client.botId):
        try:
            title, color = args.message.split("color=")
            color = color if color.startswith("#") else f'#{color}'
        except Exception:
            title = args.message
            color = None

        if args.subClient.add_title(args.authorId, title, color):
            args.subClient.send_message(args.chatId, f"The titles of {args.author} has changed")
@client.command("removetitle")
def remove_title(data):
    data.subClient.remove_title(data.authorId, data.message)
    data.subClient.send_message(chatId=data.chatId, message="removed!")
@client.command("stickmg")
def stickmg(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
	   image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
	   filename = image.split("/")[-1]
	   filetype = image.split(".")[-1]
	   if filetype!="gif":
	   	filetype = "image"
	   	urllib.request.urlretrieve(image, filename)
	   	with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
	os.remove(filename)				
@client.command("cookie")
def cookie(args):
    args.subClient.send_message(args.chatId, f"Here is a cookie for {args.author} 🍪")
@client.command("luv")
def luv(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(data.chatId, message=f"the probability of love between {msg[1]} and {msg[2]} is {random.randint(0,100)}%")
		except:
			pass        

@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")
@client.command("joinallchats")
def joinallchats(data):
	print(type(data))
	data.subClient.send_message(chatId=data.chatId, message="We go to all active chats in the community ...")
	data.subClient.join_all_chat()
	data.subClient.send_message(chatId=data.chatId, message="Located in all active chats!")
@client.command("ramen")
def ramen(args):
    args.subClient.send_message(args.chatId, f"Here are some ramen for {args.author} 🍜")
@client.command("backgr")
def backgr(data):
        image = data.subClient.get_chat_thread(chatId=data.chatId).backgroundImage
        if image:
            filename = path.basename(image)
            urllib.request.urlretrieve(image, filename)
            with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
            os.remove(filename)

@client.command("dice")
def dice(args):
    if not args.message:
        args.subClient.send_message(args.chatId, f"🎲 -{randint(1, 20)},(1-20)- 🎲")
    else:
        try:
            n1, n2 = map(int, args.message.split('d'))
            times = n1 if n1 < 20 else 20
            max_num = n2 if n2 < 1_000_000 else 1_000_000
            numbers = [randint(1, (max_num)) for _ in range(times)]

            args.subClient.send_message(args.chatId, f'🎲 -{sum(numbers)},[ {" ".join(map(str, numbers))}](1-{max_num})- 🎲')
        except Exception as e:
            print_exception(e)


@client.command("join")
def join(args):
    val = args.subClient.join_chatroom(args.message, args.chatId)
    if val or val == "":
        args.subClient.send_message(args.chatId, f"Chat {val} joined".strip())
    else:
        args.subClient.send_message(args.chatId, "No chat joined")


@client.command("joinall")
def join_all(args):
    if client.check(args, 'staff'):
        args.subClient.join_all_chat()
        args.subClient.send_message(args.chatId, "All chat joined")


@client.command("leaveall")
def leave_all(args):
    if client.check(args, 'staff'):
        args.subClient.send_message(args.chatId, "Leaving all chat...")
        args.subClient.leave_all_chats()


@client.command("leave")
def leave(args):
    if args.message:
        chat_ide = args.subClient.get_chat_id(args.message)
        if chat_ide:
            args.chatId = chat_ide
    args.subClient.leave_chat(args.chatId)


@client.command("clear")
def clear(args):
    if client.check(args, 'staff') and client.check(args, 'staff', client.botId):
        size = 1
        args.subClient.delete_message(args.chatId, args.messageId, asStaff=True, reason="Clear")

        if size > 100:
            size = 100

        messages = args.subClient.get_chat_messages(chatId=args.chatId, size=size).messageId

        for message in messages:
            with suppress(Exception):
                args.subClient.delete_message(args.chatId, message, asStaff=True)


@client.command("spam")
def spam(args):
    quantity, msg = args.message.split()
    quantity = 1 if not quantity.isdigit() else int(quantity)
    quantity = 10 if quantity > 10 else quantity

    for _ in range(quantity):
        args.subClient.send_message(args.chatId, msg)


@client.command("mention")
def mention(args):
    try:
        size = int(args.message.strip().split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 1

    val = args.subClient.get_user_id(args.message)
    if not val:
        args.subClient.send_message(chatId=args.chatId, message="Username not found")
        return

    if size > 5:
        size = 5

    if val:
        for _ in range(size):
            with suppress(Exception):
                args.subClient.send_message(chatId=args.chatId, message=f"‎‏‎‏@{val[0]}‬‭", mentionUserIds=[val[1]])


@client.command("all")
def mentionall(args):
    if client.check(args, 'staff'):
        if args.message:
            chat_ide = args.subClient.get_chat_id(args.message)
            if chat_ide:
                args.chatId = chat_ide
            args.message = " ".join(args.message.strip().split()[:-1])

        mention = [userId for userId in args.subClient.get_chat_users(chatId=args.chatId).userId]
        test = "".join(["‎‏‎‏‬‭" for user in args.subClient.get_chat_users(chatId=args.chatId).userId])

        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"@everyone{test}", mentionUserIds=mention)


@client.command("msg")
def msg(args):
    value = 0
    size = 1
    ment = None
    with suppress(Exception):
        args.subClient.delete_message(args.chatId, args.messageId, asStaff=True, reason="Clear")

    if "chat=" in args.message:
        chat_name = args.message.rsplit("chat=", 1).pop()
        chat_ide = args.subClient.get_chat_id(chat_name)
        if chat_ide:
            args.chatId = chat_ide
        args.message = " ".join(args.message.strip().split()[:-1])

    try:
        size = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        size = 0

    try:
        value = int(args.message.split().pop())
        args.message = " ".join(args.message.strip().split()[:-1])
    except ValueError:
        value = size
        size = 1

    if not args.message and value == 1:
        args.message = f"‎‏‎‏@{args.author}‬‭"
        ment = args.authorId

    if size > 10:
        size = 10

    for _ in range(size):
        with suppress(Exception):
            args.subClient.send_message(chatId=args.chatId, message=f"{args.message}", messageType=value, mentionUserIds=ment)



def Tass(data):
    listusers=[]
    for userId ,status in zip(data.profile.userId,data.profile.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers
@client.command("abw")
def add_banned_word(args):
    if client.check(args, 'staff'):
        if not args.message or args.message in args.subClient.banned_words:
            return
        try:
            args.message = args.message.lower().strip().split()
        except Exception:
            args.message = [args.message.lower().strip()]
        args.subClient.add_banned_words(args.message)
        args.subClient.send_message(args.chatId, "Banned word list updated")


@client.command("rbw")
def remove_banned_word(args):
    if client.check(args, 'staff'):
        if not args.message:
            return
        try:
            args.message = args.message.lower().strip().split()
        except Exception:
            args.message = [args.message.lower().strip()]
        args.subClient.remove_banned_words(args.message)
        args.subClient.send_message(args.chatId, "Banned word list updated")


@client.command("bwl")
def banned_word_list(args):
    val = ""
    if args.subClient.banned_words:
        for elem in args.subClient.banned_words:
            val += elem + "\n"
    else:
        val = "No words in the list"
    args.subClient.send_message(args.chatId, val)


@client.command("sw")
def sw(args):
    if client.check(args, 'staff'):
        args.subClient.set_welcome_message(args.message)
        args.subClient.send_message(args.chatId, "Welcome message changed")


@client.command("chatlist")
def get_chats(args):
    val = args.subClient.get_chats()
    for title, _ in zip(val.title, val.chatId):
        args.subClient.send_message(args.chatId, title)


@client.command("chatid")
def chat_id(args):
    val = args.subClient.get_chats()
    for title, chat_id in zip(val.title, val.chatId):
        if args.message.lower() in title.lower():
            args.subClient.send_message(args.chatId, f"{title} | {chat_id}")


@client.command("leaveamino")
def leave_amino(args):
    if client.check(args, 'staff'):
        args.subClient.send_message(args.chatId, "Leaving the amino!")
        args.subClient.leave_community()
        del client[args.subClient.community_id]


@client.command("prank")
def prank(args):
    with suppress(Exception):
        args.subClient.delete_message(args.chatId, args.messageId, asStaff=True)

    transactionId = "5b3964da-a83d-c4d0-daf3-6e259d10fbc3"
    if args.message:
        chat_ide = args.subClient.get_chat_id(args.message)
        if chat_ide:
            args.chatId = chat_ide
    for _ in range(10):
        args.subClient.pay(coins=500, chatId=args.chatId, transactionId=transactionId)


def telecharger(url):
    music = None
    if ("=" in url and "/" in url and " " not in url) or ("/" in url and " " not in url):
        if "=" in url and "/" in url:
            music = url.rsplit("=", 1)[-1]
        elif "/" in url:
            music = url.rsplit("/")[-1]

        if music in os.listdir(path_sound):
            return music

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            'extract-audio': True,
            'outtmpl': f"audio/{music}.webm",
            }

        with YoutubeDL(ydl_opts) as ydl:
            video_length = ydl.extract_info(url, download=True).get('duration')
            ydl.cache.remove()

        url = music+".mp3"

        return url, video_length
    return False, False


def decoupe(musical, temps):
    size = 170
    with open(musical, "rb") as fichier:
        nombre_ligne = len(fichier.readlines())

    if temps < 180 or temps > 540:
        return False

    decoupage = int(size*nombre_ligne / temps)

    t = 0
    file_list = []
    for a in range(0, nombre_ligne, decoupage):
        b = a + decoupage
        if b >= nombre_ligne:
            b = nombre_ligne

        with open(musical, "rb") as fichier:
            lignes = fichier.readlines()[a:b]

        with open(musical.replace(".mp3", "PART"+str(t)+".mp3"),  "wb") as mus:
            for ligne in lignes:
                mus.write(ligne)

        file_list.append(musical.replace(".mp3", "PART"+str(t)+".mp3"))
        t += 1
    return file_list


@client.command("convert")
def convert(args):
    music, size = telecharger(args.message)
    if music:
        music = f"audio/{music}"
        val = decoupe(music, size)

        if not val:
            try:
                with open(music, 'rb') as fp:
                    args.subClient.send_message(args.chatId, file=fp, fileType="audio")
            except Exception:
                args.subClient.send_message(args.chatId, "Error! File too heavy (9 min max)")
            os.remove(music)
            return

        os.remove(music)
        for elem in val:
            with suppress(Exception):
                with open(elem, 'rb') as fp:
                    args.subClient.send_message(args.chatId, file=fp, fileType="audio")
            os.remove(elem)
        return
    args.subClient.send_message(args.chatId, "Error! Wrong link")


@client.command("help")
def helper(args):
    if not args.message:
        args.subClient.send_message(args.chatId, helpMsg)
    elif args.message == "msg":
        args.subClient.send_message(args.chatId, help_message)
    elif args.message == "ask":
        args.subClient.send_message(args.chatId, helpAsk)
    else:
        args.subClient.send_message(args.chatId, "No help is available for this command")


@client.command("reboot")
def reboot(args):
    args.subClient.send_message(args.chatId, "Restarting Bot")
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])



@client.command("stop")
def stop(args):
    args.subClient.send_message(args.chatId, "Stopping Bot")
    os.execv(sys.executable, ["None", "None"])


@client.command("uinfo", False)
def uinfo(args):
    val = ""
    val2 = ""
    uid = ""
    with suppress(Exception):
        val = args.subClient.client.get_user_info(args.message)
        val2 = args.subClient.get_user_info(args.message)

    if not val:
        uid = args.subClient.get_user_id(args.message)
        if uid:
            val = args.subClient.client.get_user_info(uid[1])
            val2 = args.subClient.get_user_info(uid[1])

    if not val:
        with suppress(Exception):
            lin = args.subClient.client.get_from_code(f"http://aminoapps.com/u/{args.message}").json["extensions"]["linkInfo"]["objectId"]
            val = args.subClient.client.get_user_info(lin)

        with suppress(Exception):
            val2 = args.subClient.get_user_info(lin)

    with suppress(Exception):
        with open(path_eljson1, "w") as file:
            file.write(dumps(val.json, sort_keys=True, indent=4))

    with suppress(Exception):
        with open(path_eljson2, "w") as file:
            file.write(dumps(val2.json, sort_keys=True, indent=4))

    for i in (path_eljson1, path_eljson2):
        if os.path.getsize(i):
            txt2pdf.callPDF(i, "result.pdf")
            pages = convert_from_path('result.pdf', 150)
            file = 'result.jpg'
            for page in pages:
                page.save(file,  'JPEG')
                with open(file, 'rb') as fp:
                    args.subClient.send_message(args.chatId, file=fp, fileType="image")
                os.remove(file)
            os.remove("result.pdf")

    if not os.path.getsize(path_eljson1) and not os.path.getsize(path_eljson1):
        args.subClient.send_message(args.chatId, "Error!")


@client.command("cinfo", False)
def cinfo(args):
    val = ""
    with suppress(Exception):
        val = args.subClient.client.get_from_code(f"http://aminoapps.com/c/{args.message}")

    with suppress(Exception):
        with open(path_eljson1, "w") as file:
            file.write(dumps(val.json, sort_keys=True, indent=4))

    if os.path.getsize(path_eljson1):
        txt2pdf.callPDF(path_eljson1, "result.pdf")
        pages = convert_from_path('result.pdf', 150)
        for page in pages:
            file = 'result.jpg'
            page.save(file,  'JPEG')
            with open(file, 'rb') as fp:
                args.subClient.send_message(args.chatId, file=fp, fileType="image")
            os.remove(file)
        os.remove("result.pdf")

    if not os.path.getsize(path_eljson1):
        args.subClient.send_message(args.chatId, "Error!")


@client.command("sendinfo", False)
def sendinfo(args):
    if args.message != "":
        arguments = args.message.strip().split()
        for eljson in (path_eljson1, path_eljson2):
            if Path(eljson).exists():
                arg = arguments.copy()
                with open(eljson, 'r') as file:
                    val = load(file)
                try:
                    memoire = val[arg.pop(0)]
                except Exception:
                    args.subClient.send_message(args.chatId, 'Wrong key!')
                if arg:
                    for elem in arg:
                        try:
                            memoire = memoire[str(elem)]
                        except Exception:
                            args.subClient.send_message(args.chatId, 'Wrong key!')
                args.subClient.send_message(args.chatId, memoire)


@client.command("global")
def get_global(args):
    val = args.subClient.get_user_id(args.message)[1]
    if val:
        ide = args.subClient.client.get_user_info(val).aminoId
        args.subClient.send_message(args.chatId, f"http://aminoapps.com/u/{ide}")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("follow")
def follow(args):
    args.subClient.follow_user(args.authorId)
    args.subClient.send_message(args.chatId, "Now following you!")


@client.command("unfollow")
def unfollow(args):
    args.subClient.unfollow_user(args.authorId)
    args.subClient.send_message(args.chatId, "Unfollow!")


@client.command("stopamino", False)
def stop_amino(args):
    args.subClient.stop_instance()
    del client[args.subClient.community_id]


@client.command("block", False)
def block(args):
    val = args.subClient.get_user_id(args.message)
    if val:
        args.subClient.client.block(val[1])
        args.subClient.send_message(args.chatId, f"User {val[0]} blocked!")


@client.command("unblock", False)
def unblock(args):
    val = args.subClient.client.get_blocked_users()
    for aminoId, userId in zip(val.aminoId, val.userId):
        if args.message in aminoId:
            args.subClient.client.unblock(userId)
            args.subClient.send_message(args.chatId, f"User {aminoId} unblocked!")


@client.command("accept")
def accept(args):
    if client.check(args, 'staff'):
        if args.subClient.accept_role("", args.chatId):
            args.subClient.send_message(args.chatId, "Accepted!")
            return
        val = args.subClient.get_notices(start=0, size=25)
        for elem in val:
            print(elem["title"])
        ans = None
        res = None

        for elem in val:
            if 'become' in elem['title'] or "host" in elem['title']:
                res = elem['noticeId']
            if res:
                ans = args.subClient.accept_role(res)
            if ans:
                args.subClient.send_message(args.chatId, "Accepted!")
                return
        else:
            args.subClient.send_message(args.chatId, "Error!")


@client.command("say")
def say(args):
    audio_file = f"audio/ttp{randint(1,500)}.mp3"
    langue = list(lang.tts_langs().keys())
    if not args.message:
        args.message = args.subClient.get_chat_messages(chatId=args.chatId, size=2).content[1]
    gTTS(text=args.message, lang=choice(langue), slow=False).save(audio_file)
    try:
        with open(audio_file, 'rb') as fp:
            args.subClient.send_message(args.chatId, file=fp, fileType="audio")
    except Exception:
        args.subClient.send_message(args.chatId, "Too heavy!")
    os.remove(audio_file)


@client.command("ask")
def ask_thing(args):
    if client.check(args, 'staff'):
        lvl = ""
        boolean = 1
        if "lvl=" in args.message:
            lvl = args.message.rsplit("lvl=", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl="+lvl, "").strip()
        elif "lvl<" in args.message:
            lvl = args.message.rsplit("lvl<", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl<"+lvl, "").strip()
            boolean = 2
        elif "lvl>" in args.message:
            lvl = args.message.rsplit("lvl>", 1)[1].strip().split(" ", 1)[0]
            args.message = args.message.replace("lvl>"+lvl, "").strip()
            boolean = 3
        try:
            lvl = int(lvl)
        except ValueError:
            lvl = 20

        args.subClient.ask_all_members(args.message+f"\n[CUI]This message was sent by {args.author}\n[CUI]I am a bot and have a nice day^^", lvl, boolean)
        args.subClient.send_message(args.chatId, "Asking...")


@client.command("askstaff", False)
def ask_staff(args):
    amino_list = client.client.sub_clients()
    for commu in amino_list.comId:
        client[commu].ask_amino_staff(message=args.message)
    args.subClient.send_message(args.chatId, "Asking...")


@client.command("prefix")
def prefix(args):
    if args.message and client.check(args, "staff"):
        args.subClient.set_prefix(args.message)
        args.subClient.send_message(args.chatId, f"prefix set as {args.message}")


@client.command("lock")
def lock_command(args):
    if client.check(args, 'staff'):
        if not args.message or args.message in args.subClient.locked_command or args.message not in client.get_commands_names() or args.message in ("lock", "unlock"):
            return
        try:
            args.message = args.message.lower().strip().split()
        except Exception:
            args.message = [args.message.lower().strip()]
        args.subClient.add_locked_command(args.message)
        args.subClient.send_message(args.chatId, "Locked command list updated")


@client.command("unlock")
def unlock_command(args):
    if client.check(args, 'staff'):
        if args.message:
            try:
                args.message = args.message.lower().strip().split()
            except Exception:
                args.message = [args.message.lower().strip()]
            args.subClient.remove_locked_command(args.message)
            args.subClient.send_message(args.chatId, "Locked command list updated")


@client.command("llock")
def locked_command_list(args):
    val = ""
    if args.subClient.locked_command:
        for elem in args.subClient.locked_command:
            val += elem+"\n"
    else:
        val = "No locked command"
    args.subClient.send_message(args.chatId, val)


@client.command("alock", False)
def admin_lock_command(args):
    if not args.message or args.message not in client.get_commands_names() or args.message == "alock":
        return

    command = args.subClient.admin_locked_command
    args.message = [args.message]

    if args.message[0] in command:
        args.subClient.remove_admin_locked_command(args.message)
    else:
        args.subClient.add_admin_locked_command(args.message)

    args.subClient.send_message(args.chatId, "Locked command list updated")


@client.command("allock", False)
def locked_admin_command_list(args):
    val = ""
    if args.subClient.admin_locked_command:
        for elem in args.subClient.admin_locked_command:
            val += elem+"\n"
    else:
        val = "No locked command"
    args.subClient.send_message(args.chatId, val)


@client.command("keepu")
def keep_favorite_users(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff'):
        users = args.subClient.favorite_users
        try:
            val = args.subClient.get_user_id(args.message)
            user, userId = val[0], val[1]
        except Exception:
            args.subClient.send_message(args.chatId, "Error, user not found!")
            return
        if userId not in users:
            args.subClient.add_favorite_users(userId)
            args.subClient.send_message(args.chatId, f"Added {user} to favorite users")
            with suppress(Exception):
                args.subClient.favorite(time=1, userId=userId)
        return
    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("unkeepu")
def unkeep_favorite_users(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff'):
        users = args.subClient.favorite_users
        try:
            val = args.subClient.get_user_id(args.message)
            user, userId = val[0], val[1]
        except Exception:
            args.subClient.send_message(args.chatId, "Error, user not found!")
            return
        if userId in users:
            args.subClient.remove_favorite_users(userId)
            args.subClient.send_message(args.chatId, f"Removed {user} to favorite users")
            with suppress(Exception):
                args.subClient.unfavorite(userId=userId)
        return
    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("keepc")
def keep_favorite_chats(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff'):
        chats = args.subClient.favorite_chats
        with suppress(Exception):
            chat = args.subClient.get_from_code(f"{args.message}")
            if chat.objectId not in chats:
                args.subClient.add_favorite_chats(chat.objectId)
                args.subClient.send_message(args.chatId, "Added to favorite chats")
            return

        val = args.subClient.get_chats()

        for title, chatId in zip(val.title, val.chatId):
            if args.message == title and chatId not in chats:
                args.subClient.add_favorite_chats(chatId)
                args.subClient.send_message(args.chatId, f"Added {title} to favorite chats")
                with suppress(Exception):
                    args.subClient.favorite(time=1, chatId=args.chatId)
                return

        for title, chatId in zip(val.title, val.chatId):
            if args.message.lower() in title.lower() and chatId not in chats:
                args.subClient.add_favorite_chats(chatId)
                args.subClient.send_message(args.chatId, f"Added {title} to favorite chats")
                with suppress(Exception):
                    args.subClient.favorite(time=1, chatId=chatId)
                return
    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("unkeepc")
def unkeep_favorite_chats(args):
    if args.subClient.is_in_staff(client.botId) and client.check(args, 'staff'):
        chats = args.subClient.favorite_chats

        with suppress(Exception):
            chat = args.subClient.get_from_code(f"{args.message}")
            if chat.objectId in chats:
                args.subClient.remove_favorite_chats(chat.objectId)
                args.subClient.send_message(args.chatId, "Removed to favorite chats")
            return

        val = args.subClient.get_chats()

        for title, chatid in zip(val.title, val.chatId):
            if args.message == title and chatid in chats:
                args.subClient.remove_favorite_chats(chatid)
                args.subClient.unfavorite(chatId=chatid)
                args.subClient.send_message(args.chatId, f"Removed {title} to favorite chats")
                return

        for title, chatid in zip(val.title, val.chatId):
            if args.message.lower() in title.lower() and chatid in chats:
                args.subClient.remove_favorite_chats(chatid)
                args.subClient.unfavorite(chatId=chatid)
                args.subClient.send_message(args.chatId, f"Removed {title} to favorite chats")
                return

    elif not client.check(args, 'staff', id_=client.botId):
        args.subClient.send_message(args.chatId, "The bot need to be in the staff!")
    else:
        args.subClient.send_message(args.chatId, "Error!")


@client.command("welcome")
def welcome_channel(args):
    if client.check(args, 'staff'):
        args.subClient.set_welcome_chat(args.chatId)
        args.subClient.send_message(args.chatId, "Welcome channel set!")


@client.command("unwelcome")
def unwelcome_channel(args):
    if client.check(args, 'staff'):
        args.subClient.unset_welcome_chat()
        args.subClient.send_message(args.chatId, "Welcome channel unset!")


@client.command("level")
def level(args):
    if client.check(args, 'staff'):
        try:
            args.message = int(args.message)
        except Exception:
            args.subClient.send_message(args.chatId, "Error, wrong level")
            return
        if args.message > 20:
            args.message = 20
        if args.message < 0:
            args.message = 0
        args.subClient.set_level(args.message)
        args.subClient.send_message(args.chatId, f"Level set to {args.message}!")


@client.command("taxe", False)
def taxe(args):
    coins = args.subClient.get_wallet_amount()
    if coins >= 1:
        amt = 0
        while coins > 500:
            args.subClient.pay(500, chatId=args.chatId)
            coins -= 500
            amt += 500
        args.subClient.pay(int(coins), chatId=args.chatId)
        args.subClient.send_message(args.chatId, f"Sending {coins+amt} coins...")
    else:
        args.subClient.send_message(args.chatId, "Account is empty!")


helpMsg = f"""
[CB]-- COMMON COMMAND --

• help (command)\t:  show this or the help associated to the command
• title (title)\t:  edit titles*
• dice (xdy)\t:  return x dice y (1d20) per default
• join (chat)\t:  join the specified channel
• mention (user)\t: mention an user
• spam (amount)\t: spam an message (limited to 10)
• msg (type)\t: send a "special" message (limited to 10)
• bwl\t:  the list of banneds words*
• llock\t: the list of locked commands
• chatlist\t: the list of public chats
• global (user)\t: give the global profile of the user
• leave\t:  leave the current channel
• follow\t: follow you
• unfollow\t: unfollow you
• audio\t: will send audio
• image\t: will send an image
• say\t: will say the message in audio
• ramen\t:  give ramens!
• cookie\t:  give a cookie!
\n
[CB]-- STAFF COMMAND --

• accept\t: accept the staff role
• abw (word list)\t:  add a banned word to the list*
• rbw (word list)\t:  remove a banned word from the list*
• sw (message)\t:  set the welcome message for new members (will start as soon as the welcome message is set)
• welcome\t:  set the welcome channel**
• unwelcome\t:  unset the welcome channel**
• ask (message)(lvl=)\t: ask to all level (lvl) something**
• clear (amount)\t:  clear the specified amount of message from the chat (max 50)*
• joinall\t:  join all public channels
• leaveall\t:  leave all public channels
• leaveamino\t: leave the community
• all\t: mention all the users of a channel
• lock (command)\t: lock the command (nobody can use it)
• unlock (command)\t: remove the lock for the command
• prefix (prefix)\t: set the prefix for the amino
• level (level)\t: set the level required for the commands
• keepu (user)\t: keep in favorite an user*
• unkeepu (user)\t: remove from favorite an user*
• keepc (chat)\t: keep in favorite a chat*
• unkeepc (chat)\t: remove from favorite a chat*
\n
[CB]-- SPECIAL --

• joinamino (amino id): join the amino (you need to be in the amino's staff)**
• uinfo (user): will give informations about the user²
• cinfo (aminoId): will give informations about the community²
• sendinfo (args): send the info from uinfo or cinfo²
• alock (command): lock or unlock the command for everyone except the owenr of the bot²
• allock\t: the list of the admin locked commands²

[CB]-- NOTE --

*(only work if bot is in staff)
**(In developpement)
²(only for devlopper or bot owner)

[CI]You want to support my work? You can give me AC!^^

[C]-- all commands are available for the owner of the bot --
[C]-- Bot made by @The_Phoenix --
[C]--Version : {version}--
"""


help_message = """
--MESSAGES--

0 - BASE
1 - STRIKE
50 - UNSUPPORTED_MESSAGE
57 - REJECTED_VOICE_CHAT
58 - MISSED_VOICE_CHAT
59 - CANCELED_VOICE_CHAT
100 - DELETED_MESSAGE
101 - JOINED_CHAT
102 - LEFT_CHAT
103 - STARTED_CHAT
104 - CHANGED_BACKGROUND
105 - EDITED_CHAT
106 - EDITED_CHAT_ICON
107 - STARTED_VOICE_CHAT
109 - UNSUPPORTED_MESSAGE
110 - ENDED_VOICE_CHAT
113 - EDITED_CHAT_DESCRIPTION
114 - ENABLED_LIVE_MODE
115 - DISABLED_LIVE_MODE
116 - NEW_CHAT_HOST
124 - INVITE_ONLY_CHANGED
125 - ENABLED_VIEW_ONLY
126 - DISABLED_VIEW_ONLY

- chat="chatname": will send the message in the specified chat
"""

helpAsk = """
Example :
- !ask Hello! Can you read this : [poll | http://aminoapp/poll]? Have a nice day!^^ lvl=6
"""

client.launch()


def filter_message(message, code):
    return normalize('NFD', message).encode(code, 'ignore').decode().lower().translate(str.maketrans("", "", punctuation))

@client.command("randemoji")
def randemoji(data):
	lis = ['😰😨😱😓🤯', '😎🤡🥴🤕🌚', '🌝🥸👻🎃', '😺👹😈😇💩', '😛😉😊😘🥳', '🤣😀😆🥰🙂', '☺️😑🙃😶🤗', '🤩😋😔😌☺️', '🤫🤐🥺🙄🤔', '🧐😤😠😳🤯', '😓😥😩😖😵', '🌞🤮🤧🤒🎃', '😍😚🤭🥲😄', '😃😂🤣😭😰', '🤬😡😮😯😲', '🤓🤑🤠😇😷', '🥵🥶👺☠️👽', '😸😹😺😻😼', '😽🙀😿😾💀', '❤️🧡💛💚💙', '💜🤎🖤🤍♥️', '💘💝💖💗💓', '💞💕💌💟❣️', '💔💋👅👄👀', '🦾🦠🦷🏵️💐', '🧝🧙🧛🧟🥷', '😪😴🥱🤤🙄', '👿😈🔥⭐🌟', '🎊🎉🕳️💤💦', '🌜👻🤖💢⚡', '✨💫👁️🍂☀️', '🧠🫀🫁🩸🌡️', '👉👌🍺🍷👄', '🦁🐻🐼🐨🐹', '🐭🐷🐸🙉🐶', '🌌🌠🌉🌆🌃', '🕊️🦅🐦🦥🦏', '🐲🦖🐢🦮🐈', '🐐🦬🐖🐑🐆', '🦍🦧🐿️🦦🦈', '🐝🐠🐋🦋🐜', '🍔🍖🍗🌭🥪', '🥞🍳🫓🌮🍕', '🍉🍓🍒🫐🍎', '🧆🥙🥘🍜🦪', '🍧🍱🥟🍚🍢', '🍰🍙🍡🍣🍟', '🧇🥯🌯🥟🥡', '🍭🍩🍪🥮🍨', '🥗🍲🫕🍥🍿', '🥃🍾🍹🍸🍻', '🅿️🅾️🆘ℹ️🖕🏿', '🤏✋👊🙌👇', '👾🕹️🎮🎲🃏', '💵💴💶💷💰', '🇺🇸🇹🇨🇸🇻🇺🇦🇼🇸', '🏤🏣🏨🏥🏩']	
	data.subClient.send_message(data.chatId, message=str(random.choice(lis)))
@client.command("fancytext")
def fancytext(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	data.subClient.send_message(data.chatId, message=fancy.light(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.bold(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.box(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.sorcerer(msg[1]))

@client.command("comment")
def comment_profile(data):
	data.subClient.comment(message="Painting from http://aminoapps.com/p/5kk6y48😎 I wish you all the best!", userId=data.authorId)
	data.subClient.send_message(data.chatId, message="The bot left you a painting on the wall!")
@client.command("profileinfo")
def profileinfo(data):
	repa = data.subClient.get_user_info(data.authorId).reputation
	lvl = data.subClient.get_user_info(data.authorId).level
	crttime = data.subClient.get_user_info(data.authorId).createdTime
	followers = data.subClient.get_user_achievements(data.authorId).numberOfFollowersCount
	profilchange = data.subClient.get_user_info(data.authorId).modifiedTime
	commentz = data.subClient.get_user_info(data.authorId).commentsCount
	posts = data.subClient.get_user_achievements(data.authorId).numberOfPostsCreated
	followed = data.subClient.get_user_info(data.authorId).followingCount
	sysrole = data.subClient.get_user_info(data.authorId).role
	data.subClient.send_message(data.chatId, message=f"""
[C]Nickname: {data.author}
[C]UserId: {data.authorId}
[C]Account created time: {crttime}
[C]Last time the profile was changed: {profilchange}
[C]Reputation number: {repa}
[C]Account level: {lvl}
[C]Number of posts created in the profile: {posts}
[C]Number of comments on the profile wall: {commentz}
[C]The number of people you follow: {followed}
[C]Account followers: {followers}
[C]Account number in system: {sysrole}
	""")

client.launch()
################################################commands/команды#############################################
def tradlist(sub):
    sublist = []
    for elem in sub:
        try:
            sublist.append(client.get_from_code(f"http://aminoapps.com/u/{elem}").objectId)
            continue
        except Exception:
            pass
        sublist.append(elem)
    return sublist


whitefile = 'whitelist.txt'
whitelist = []
try:
    with open(whitefile, 'r') as file:
        for whitelistmember in file.readlines():
            whitelist.append(whitelistmember.strip())
except FileNotFoundError:
    a = open(whitefile, "w")
    a.close()


whitelist = tradlist(whitelist)


def is_whitelisted(data):
    if any(user in data.authorId for user in whitelist):
        return True
    data.subClient.send_message(chatId=data.chatId, message="You don't have permissions")
    return False
@client.on_message()
def text_message(args):
    # print(f"{args.author} : {args.message}")
    pass
    

@client.event("on_chat_invite")
def on_chat_invite(data):
    try:
        commuId = data.json["ndcId"]
        subClient = client.get_community(commuId)
    except Exception:
        return

    args = Parameters(data, subClient)

    subClient.join_chatroom(chatId=args.chatId)
    subClient.send_message(args.chatId, f"Hello!\n[B]I am a bot, if you have any question ask a staff member!\nHow can I help you?\n(you can do {subClient.prefix}help if you need help)")

#@client.on_all()
def on_message(data) -> None:
    content = data.message
    mtype = data.info.message.type
    if mtype != 0 and content and str(data.info.comId):
        data.subClient.kick(chatId=data.chatId, userId=data.authorId, allowRejoin=False)
        data.subClient.send_message(data.chatId, f'Anti-Raid-Bot : MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
        data.subClient.delete_message(data.chatId, data.messageId, asStaff=True, reason=f'Anti-Raid-Bot : MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
        return
        try:
            data.subClient.ban(data.authorId, f'Anti-Raid-Bot : MessageType {mtype} detected! Nickname: {data.author} | userId: {data.authorId} | messageId: {data.messageId}.')
        except Exception:
            pass

print("Ready")

def maintenance():
    print("launch maintenance")
    i = 0
    while i < 7200:
        i += 10
        time.sleep(10)
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])


client.launch(True)
Thread(target=maintenance).start()

def reconsocketloop():
	while True:
		client.close()
		client.start()
		sleep(120)


socketloop = threading.Thread(target=reconsocketloop, daemon=True)
socketloop.start()

print("Ready")


