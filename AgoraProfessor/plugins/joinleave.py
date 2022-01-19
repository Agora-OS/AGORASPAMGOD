import asyncio
from AgoraProfessor import AGORA, AGORA2, AGORA3, AGORA4, AGORA5 , AGORA6, AGORA7, AGORA8, AGORA9, AGORA10, AGORA11, AGORA12, AGORA13, AGORA14, AGORA15, AGORA16, AGORA17, AGORA18, AGORA19, AGORA20, AGORA21, AGORA22, AGORA23, AGORA24, AGORA25, AGORA26, AGORA27, AGORA28, AGORA29, AGORA30, AGORA31, AGORA32, AGORA33, AGORA34, AGORA35, AGORA36, AGORA37, AGORA38, AGORA39, AGORA40, SUDO_USERS
from .. import CMD_HNDLR as hl
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events
import os
import random
import sys


@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SUDO_USERS:
        AGORASPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = AGORASPAM[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Joined Successfully ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/abcdefghijklmsnob\n\n.pjoin abcdefghijklmsnob"
    if e.sender_id in SUDO_USERS:
        AGORASPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = AGORASPAM[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Joined Successfully (Private Group/channel) ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



#leave 
@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        AGORASPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = AGORASPAM[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left ☑️")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
