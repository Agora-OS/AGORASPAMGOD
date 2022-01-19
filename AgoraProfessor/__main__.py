import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from AgoraProfessor.utils import load_plugins
import logging
from telethon import events
from . import AGORA, AGORA2, AGORA3, AGORA4, AGORA5 , AGORA6, AGORA7, AGORA8, AGORA9, AGORA10, AGORA11, AGORA12, AGORA13, AGORA14, AGORA15, AGORA16, AGORA17, AGORA18, AGORA19, AGORA20, AGORA21, AGORA22, AGORA23, AGORA24, AGORA25, AGORA26, AGORA27, AGORA28, AGORA29, AGORA30, AGORA31, AGORA32, AGORA33, AGORA34, AGORA35, AGORA36, AGORA37, AGORA38, AGORA39, AGORA40

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "AgoraProfessor/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("🎉🎊🥳 AGORA  GANGSTER Successfully deployed 🥳🎊🎉")
print("Enjoy! Do visit @AGORA_SPAM_OFFICIAL")

if len(argv) not in (1, 3, 4):
    try:
        AGORA.disconnect()
    except Exception as e:
        pass
    try:
        AGORA2.disconnect()
    except Exception as e:
        pass
    try:
        AGORA3.disconnect()
    except Exception as e:
        pass
    try:
        AGORA4.disconnect()
    except Exception as e:
        pass
    try:
        AGORA5.disconnect()
    except Exception as e:
        pass
    try:
        AGORA6.disconnect()
    except Exception as e:
        pass
    try:
        AGORA7.disconnect()
    except Exception as e:
        pass
    try:
        AGORA8.disconnect()
    except Exception as e:
        pass
    try:
        AGORA9.disconnect()
    except Exception as e:
        pass
    try:
        AGORA10.disconnect()
    except Exception as e:
        pass
    try:
        AGORA11.disconnect()
    except Exception as e:
        pass
    try:
        AGORA12.disconnect()
    except Exception as e:
        pass
    try:
        AGORA13.disconnect()
    except Exception as e:
        pass
    try:
        AGORA14.disconnect()
    except Exception as e:
        pass
    try:
        AGORA15.disconnect()
    except Exception as e:
        pass
    try:
        AGORA16.disconnect()
    except Exception as e:
        pass
    try:
        AGORA17.disconnect()
    except Exception as e:
        pass
    try:
        AGORA18.disconnect()
    except Exception as e:
        pass
    try:
        AGORA19.disconnect()
    except Exception as e:
        pass
    try:
        AGORA20.disconnect()
    except Exception as e:
        pass
    try:
        AGORA21.disconnect()
    except Exception as e:
        pass
    try:
        AGORA22.disconnect()
    except Exception as e:
        pass
    try:
        AGORA23.disconnect()
    except Exception as e:
        pass
    try:
        AGORA24.disconnect()
    except Exception as e:
        pass
    try:
        AGORA25.disconnect()
    except Exception as e:
        pass
    try:
        AGORA26.disconnect()
    except Exception as e:
        pass
    try:
        AGORA27.disconnect()
    except Exception as e:
        pass
    try:
        AGORA28.disconnect()
    except Exception as e:
        pass
    try:
        AGORA29.disconnect()
    except Exception as e:
        pass
    try:
        AGORA30.disconnect()
    except Exception as e:
        pass
    try:
        AGORA31.disconnect()
    except Exception as e:
        pass
    try:
        AGORA32.disconnect()
    except Exception as e:
        pass
    try:
        AGORA33.disconnect()
    except Exception as e:
        pass
    try:
        AGORA34.disconnect()
    except Exception as e:
        pass
    try:
        AGORA35.disconnect()
    except Exception as e:
        pass
    try:
        AGORA36.disconnect()
    except Exception as e:
        pass
    try:
        AGORA37.disconnect()
    except Exception as e:
        pass
    try:
        AGORA38.disconnect()
    except Exception as e:
        pass
    try:
        AGORA39.disconnect()
    except Exception as e:
        pass
    try:
        AGORA40.disconnect()
    except Exception as e:
        pass
else:
    try:
        AGORA.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA30.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA31.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA32.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA33.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA34.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA35.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA36.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA37.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA38.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA39.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AGORA40.run_until_disconnected()
    except Exception as e:
        pass
