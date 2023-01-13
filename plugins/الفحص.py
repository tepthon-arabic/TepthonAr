from plugins import ultroid_cmd
from . import get_help

__doc__ = get_help("help_bot")

import os
import sys
import time
from platform import python_version as pyver
from random import choice

from telethon import __version__
from telethon.errors.rpcerrorlist import (
    BotMethodInvalidError,
    ChatSendMediaForbiddenError,
)

from pyUltroid.version import __version__ as UltVer

from . import HOSTED_ON, LOGS

try:
    from git import Repo
except ImportError:
    LOGS.error("bot: 'gitpython' module not found!")
    Repo = None

from telethon.utils import resolve_bot_file_id

from . import (
    OWNER_NAME,
    start_time,
    time_formatter,
    ultroid_version,)


@ultroid_cmd(pattern="فحص")
    ANIME = None
    repthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    if "ANIME" in repthon_caption:
        data = requests.get("https://animechan.vercel.app/api/random").json()
        ANIME = f"**“{data['quote']}” - {data['character']} ({data['anime']})**"
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    repthonevent = await edit_or_reply(event, "** ᯽︙ يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "⿻┊‌"
    ALIVE_TEXT = (
        gvarstatus("ALIVE_TEXT") or "**父[ 𝚃𝙴𝙿𝚃𝙷𝙾𝙽 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 ✓ ](t.me/Tepthone)父**"
    )
    REPTHON_IMG = gvarstatus("ALIVE_PIC")
    caption = repthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        ANIME=ANIME,
        EMOJI=EMOJI,
        mention=OWNER_NAME,
        uptime=uptime,
        telever=version.__version__,
        UltVer=ultroid_version,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if REPTHON_IMG:
        REPTHON = list(REPTHON_IMG.split())
        PIC = random.choice(REPTHON)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await repthonevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                repthonevent,
                f"**رابط الصورة غير صحيح**\nعليك الرد على رابط الصورة ب .اضف صورة الفحص",
            )
    else:
        await edit_or_reply(
            repthonevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**‎{EMOJI}‌‎𝙽𝙰𝙼𝙴 𖠄 {OWNER_NAME}** ٫
**‌‎{EMOJI}‌‎𝙿𝚈𝚃𝙷𝙾𝙽 𖠄 {pyver}** ٫
**‌‎{EMOJI}‌‎𝚁𝚎𝚙𝚝𝚑𝚘𝚗 𖠄 {telever}** ٫
**‌‎{EMOJI}‌‎𝚄𝙿𝚃𝙸𝙼𝙴 𖠄 {uptime}** ٫
‌‎**{EMOJI}‌‎‌‎𝙿𝙸𝙽𝙶 𖠄 {ping}** ٫
**𖠄 𝗧𝗘𝗣𝗧𝗛𝗢𝗡 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𖠄**"""


def repthonalive_text():
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    jmthon_caption = "**سورس تيبثون يعمل بنجاح**\n"
    jmthon_caption += f"**{EMOJI} اصدار التيليثون :** `{version.__version__}\n`"
    jmthon_caption += f"**{EMOJI} اصدار ريبثون :** `{OWNER_NAME}`\n"
    jmthon_caption += f"**{EMOJI} اصدار البايثون :** `{python_version()}\n`"
    jmthon_caption += f"**{EMOJI} المالك:** {mention}\n"
    return repthon_caption
