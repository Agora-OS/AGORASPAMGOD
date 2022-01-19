import random
import asyncio
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from resources.data import DEADLYSPAM, RAID
from AgoraProfessor import AGORA, AGORA2, AGORA3, AGORA4, AGORA5 , AGORA6, AGORA7, AGORA8, AGORA9, AGORA10, AGORA11, AGORA12, AGORA13, AGORA14, AGORA15, AGORA16, AGORA17, AGORA18, AGORA19, AGORA20, AGORA21, AGORA22, AGORA23, AGORA24, AGORA25, AGORA26, AGORA27, AGORA28, AGORA29, AGORA30, AGORA31, AGORA32, AGORA33, AGORA34, AGORA35, AGORA36, AGORA37, AGORA38, AGORA39, AGORA40, SUDO_USERS
from .. import CMD_HNDLR as hl


@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
async def _(e):   
    usage = "**MODULE NAME** : **DM**\n\n command: \n\n .dm <username> <massage> \n .dm <reply to the use> <massage>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        AGORASPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(AGORASPAM) == 2:
            user = str(AGORASPAM[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in AGORASPAM:
                text = f"I can't Dm to @AGORA_SPAM_OFFICIAL's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:            
                 message = str(AGORASPAM[1])
                 await e.reply("🔸Message Delivered🔸")
                 await e.client.send_message(g, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in AGORASPAM:
                text = f"I can't Dm to @AGORA_SPAM_OFFICIAL's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(AGORASPAM[0])
                await e.reply("🔸 Message Delivered 🔸")
                await e.client.send_message(g, message)
                await asyncio.sleep(0.3)

        else:
             await e.reply(usage)


@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
async def dmraid(e):
    usage = "**MODULE NAME** : **DM RAID**\n\n command: \n\n .dmraid <count> <username> \n .dmraid <reply to the use> <massage>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        AGORASPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(AGORASPAM) == 2:
            user = str(AGORASPAM[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYSPAM:
                text = f"I can't raid on @AGORA_SPAM_OFFICIAL's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(DEADLYSPAM[0])
                await e.reply("⚜️ Dm Raid Started Successfully ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.4)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in AGORASPAM:
                text = f"I can't raid on @AGORA_SPAM_OFFICIAL's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(DEADLYSPAM[0])
                await e.reply("⚜️ Dm Raid Strated Successfully!! ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)
