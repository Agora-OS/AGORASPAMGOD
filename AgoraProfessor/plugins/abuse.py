import asyncio
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from OfficialSameer import AGORA, AGORA2, AGORA3, AGORA4, AGORA5 , AGORA6, AGORA7, AGORA8, AGORA9, AGORA10, AGORA11, AGORA12, AGORA13, AGORA14, AGORA15, AGORA16, AGORA17, AGORA18, AGORA19, AGORA20, AGORA21, AGORA22, AGORA23, AGORA24, AGORA25, AGORA26, AGORA27, AGORA28, AGORA29, AGORA30, AGORA31, AGORA32, AGORA33, AGORA34, AGORA35, AGORA36, AGORA37, AGORA38, AGORA39, AGORA40, SUDO_USERS
from resources.data import AGORASPAM
from .. import CMD_HNDLR 
  
    
@AGORA.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA2.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA3.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA4.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA5.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA6.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA7.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA8.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA9.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA10.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA11.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA12.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA13.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA14.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA15.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA16.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA17.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA18.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA19.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA20.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA21.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAMMA22.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA23.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA24.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA25.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA26.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA27.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA28.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA29.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA30.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA31.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA32.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA33.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA34.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA35.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA36.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA37.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA38.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA39.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@AGORA40.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
async def _(e):
    usage = "**Module Name = Abuse**\n\nCommand:\n\n .gali <Username of User>\n\nit will continuously abuse until you restart!!."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        AGORASPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(AGORASPAM) == 1:
            user = str(AGORASPAM[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in AGORASPAM:
                text = f"I can't abuse @AGORA_SPAM_OFFICIAL's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                name = f"[{c}](tg://user?id={g})"
                caption1 =f"{name} GAND FATT GYII KYA HIJDE KI OLAAD"
                caption2 =f"{name} **RANDI KE PILLLE**"
                caption3 =f" {name} 𝑪𝑯𝑯𝑯𝑯𝑯𝑼𝑼𝑼𝑼𝑼𝑫𝑫𝑫𝑫 𝑮𝒀𝑨𝑨𝑨𝑨𝑨𝑨𝑨 𝑳𝑶𝑽𝑽𝑽𝑽𝑽𝑫𝑫𝑬𝑬 𝑻𝑼𝑼𝑼𝑼"
                caption4 =f" {name} 𝕋𝕖𝕣𝕚 𝕄𝕒𝕒 𝕂𝕚 𝕏𝕙𝕠𝕥 𝕓𝕒𝕕𝕙𝕧𝕖"
                caption5 =f"{name} **ISKE MAAKI CHUTT LELO FREE FULL NIGHT**"
                caption6 =f" {name} __TERE MAAKI CHUTT MASTT SOFT SOFT HE__ 🤤"
                caption7 =f"# {name} TERE MAAKI CHUT ME AGORA KE LUNDD"
                caption8 =f"{name} **RAANDD KAA PILLAAA**"
                caption9 =f"{name} 𝙄𝙎𝙆𝙄 𝘽𝙃𝙀𝙉 𝙋𝙍𝙊𝙁𝙀𝙎𝙎𝙊𝙍 𝙆 𝙇𝙐𝙉𝘿 𝘾𝙃𝙊𝙊𝙎𝙏𝙄𝙄 𝙃𝙀"
                caption10 =f"{name} __AGAYA SWADH__"
                caption11 =f"{name} **TERI MAAA**"
                caption12 =f"**MERE SE**"
                caption13 =f"**Rozz CHUDTII**"
                caption14 =f"__Haiii__"
                caption15 =f"{name} TERE BHEN KO CHODU"
                caption16 =f"🆃🅰🅿🅰"
                caption17 =f"🆃🅰🅿"
                caption18 =f"🆃🅰🅿🅰"
                caption18 =f"🆃🅰🅿"
                caption20 =f"__NON STOP__"
                caption21 =f"{name} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗔𝗚𝗢𝗥𝗔 𝗞 𝗟𝗨𝗡𝗗 𝗟𝗘 𝗡𝗔𝗖𝗛𝗧𝗜 𝗛𝗘"
                caption22 =f"🤤"
                caption23 =f"{name} __TERI MAA MST ARAAM DETI HE__🤤🤤"
                caption24 =f"{name} __KE BHEN KI CHUT LELO FULL NIGHT FREEE__"
                caption25 =f"{name} __KI BHEN RANDIII__"
                caption26 =f"{name} __ISKE BHEN MST MARI RANDI__ 🤤🤤"
                caption27 =f"😂🖕🤣"
                caption28 =f"😂"
                caption29 =f"__EK RUPAY KI PEPSI {name} KI BEHAN SEXYY__"
                caption30 =f"{name} **ISKI BHEN MERI PERSONAL HE MENE BOHOT CHODAA HE USKO__ \n\n __DM {name} FOR PERSONAL RANDI__"
                fuk = e.chat_id
                async with e.client.action(fuk, "typing"):
                        await e.client.send_message(fuk, caption1)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption2)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption3)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption4)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption5)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption6)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption7)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption8)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption9)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption10)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption11)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption12)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption13)
                        await asyncio.sleep(0.4)
                        await e.client.send_message(fuk, caption14)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption15)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption16)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption17)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption18)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption19)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption20)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption21)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption22)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption23)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption24)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption25)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption26)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption27)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption28)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption29)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption30)
                        await asyncio.sleep(0.3)

        else:
             await e.reply(usage)
