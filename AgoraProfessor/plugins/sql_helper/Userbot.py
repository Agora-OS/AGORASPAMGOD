# DEADLY X Spam - Spam Userbots
# © 2021 - 2022 - TheDEADLY

import os
import sys
from OfficialSameer import AGORA, AGORA2, AGORA3, AGORA4, AGORA5 , AGORA6, AGORA7, AGORA8, AGORA9, AGORA10, AGORA11, AGORA12, AGORA13, AGORA14, AGORA15, AGORA16, AGORA17, AGORA18, AGORA19, AGORA20, AGORA21, AGORA22, AGORA23, AGORA24, AGORA25, AGORA26, AGORA27, AGORA28, AGORA29, AGORA30, AGORA31, AGORA32, AGORA33, AGORA34, AGORA35, AGORA36, AGORA37, AGORA38, AGORA39, AGORA40, SUDO_USERS
from OfficialSameer import ALIVE_PIC, deadlyversion
from .. import CMD_HNDLR as hl
from telethon import events, version
from time import time
from datetime import datetime

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        if e.reply_to_msg_id:
            fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
        else:
            fuk = await e.reply("Pᴏɴɢ!!.....")
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        pingop =             f"😁 🇵 🇴 🇳 🇬 !\n\n♡︎ `{ms}` 𝗺𝘀 ♡︎"                   
        await fuk.edit(pingop)


# ALIVE

AGORA_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/96754711395c8cd65553c.jpg"


AGORASPAM = "🔥 𝐀𝐆𝐎𝐑𝐀 𝐆𝐀𝐍𝐆𝐒𝐓𝐄𝐑𝐒 🔥 \n\n"

AGORASPAM += f"┏━━━━━━━━━━━━━━━━━━━\n"

AGORASPAM += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
                           
AGORASPAM += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

AGORASPAM += f"┣➣ **ᴀɢᴏʀᴀ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
    
AGORASPAM += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/AGORA_SPAM_OFFICIAL)\n"

AGORASPAM += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/AGORABOT_INFO)\n"

AGORASPAM += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

AGORASPAM += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/Agora-OS/AGORASPAMGOD) 🖤"            
                                    
@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await SAM.send_file(event.chat_id,
                                  AGORA_PIC,
                                  caption=AGORASPAM)
   
   
# help

HELP_PIC = "https://te.legra.ph/file/792fa83b58082149766a9.jpg"

AGORASPAM = "🔥 AGORA SPAM GOD 🔥\n\n"
 
AGORASPAM += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅᴇᴀᴅʟʏ sᴘᴀᴍ ʙᴏᴛ__\n\n"

AGORASPAM += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

AGORASPAM += f" `.ping` - `.alive` - `.setname` - `.setbio` - `.inviteall` - .`restart` - `.update` - `.stats` - `.addsudo` \n\n"
 
AGORASPAM += f" ↧ 𝙹𝙾𝙸𝙽/𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂 ↧\n\n"

AGORASPAM += f" `.join` - `.pjoin` - `.leave`\n\n"
 
AGORASPAM += f" ↧ 𝚂𝙿𝙰𝙼 / 𝚁𝙰𝙸𝙳 𝙲𝙼𝙳𝚂 ↧\n\n"

AGORASPAM += f" `.raid` - `.replyraid` - `.dreplyraid` - `.delayraid` \n\n `.spam` - `.bigspam` - `.delayspam` - `.abuse` \n\n"

AGORASPAM += f" 𝙳𝙼 / 𝙴𝚌𝚑𝚘 𝙲𝚖𝚍𝚜 \n\n"

AGORASPAM += f" `.dm` - `.dmraid` - `.dmspam` \n\n `.addecho` - `.rmecho` \n\n"

AGORASPAM += f"All Cmds Uploaded : [•HERE•](https://t.me/AGORA_SPAM_OFFICIAL/88) \n\n"
                                                         
AGORASPAM += f"© @AGORASWAMY_PROFESSOR | @AGORABOT_INFO\n"


@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await SAM.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=AGORASPAM)                                                         


@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA22.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝙍𝙀𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂\n\n ....RUKO ZARA SABR KARO TERA HI KAAM KAR RAH HU BC"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await AGORA.disconnect()
        except Exception:
            pass
        try:
            await AGORA2.disconnect()
        except Exception:
            pass
        try:
            await AGORA3.disconnect()
        except Exception:
            pass
        try:
            await AGORA4.disconnect()
        except Exception:
            pass
        try:
            await AGORA5.disconnect()
        except Exception:
            pass
        try:
            await AGORA6.disconnect()
        except Exception:
            pass
        try:
            await AGORA7.disconnect()
        except Exception:
            pass
        try:
            await AGORA8.disconnect()
        except Exception:
            pass
        try:
            await AGORA9.disconnect()
        except Exception:
            pass
        try:
            await AGORA10.disconnect()
        except Exception:
            pass
        try:
            await AGORA11.disconnect()
        except Exception:
            pass
        try:
            await AGORA12.disconnect()
        except Exception:
            pass
        try:
            await AGORA13.disconnect()
        except Exception:
            pass
        try:
            await AGORA14.disconnect()
        except Exception:
            pass
        try:
            await AGORA15.disconnect()
        except Exception:
            pass
        try:
            await SAM16.disconnect()
        except Exception:
            pass
        try:
            await AGORA17.disconnect()
        except Exception:
            pass
        try:
            await AGORA18.disconnect()
        except Exception:
            pass
        try:
            await AGORA19.disconnect()
        except Exception:
            pass
        try:
            await AGORA20.disconnect()
        except Exception:
            pass
        try:
            await AGORA21.disconnect()
        except Exception:
            pass
        try:
            await AGORA22.disconnect()
        except Exception:
            pass
        try:
            await AGORA23.disconnect()
        except Exception:
            pass
        try:
            await AGORA24.disconnect()
        except Exception:
            pass
        try:
            await AGORA25.disconnect()
        except Exception:
            pass
        try:
            await AGORA26.disconnect()
        except Exception:
            pass
        try:
            await AGORA27.disconnect()
        except Exception:
            pass
        try:
            await AGORA28.disconnect()
        except Exception:
            pass
        try:
            await AGORA29.disconnect()
        except Exception:
            pass
        try:
            await AGORA30.disconnect()
        except Exception:
            pass
        try:
            await AGORA31.disconnect()
        except Exception:
            pass
        try:
            await AGORA32.disconnect()
        except Exception:
            pass
        try:
            await AGORA33.disconnect()
        except Exception:
            pass
        try:
            await AGORA34.disconnect()
        except Exception:
            pass
        try:
            await AGORA35.disconnect()
        except Exception:
            pass
        try:
            await AGORA36.disconnect()
        except Exception:
            pass
        try:
            await AGORA37.disconnect()
        except Exception:
            pass
        try:
            await AGORA38.disconnect()
        except Exception:
            pass
        try:
            await AGORA39.disconnect()
        except Exception:
            pass
        try:
            await AGORA40.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
