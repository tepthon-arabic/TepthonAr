# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}اضف مميز <word><reply to a message>`
    اضف الشخص مميز عن طريق الرد.

• `{i}مسح مميز <word>`
    مسح الشخص مميز..

• `{i}قائمة المميزين`
    قائمة المميزين جميعهم.

• Use :
    type `$(ur snip word)` get setted reply.
"""
import os

from telegraph import upload_file as uf
from telethon.utils import pack_bot_file_id

from pyUltroid._misc import sudoers
from pyUltroid.dB.snips_db import add_snip, get_snips, list_snip, rem_snip
from pyUltroid.fns.tools import create_tl_btn, format_btn, get_msg_button

from . import events, get_string, mediainfo, udB, ultroid_bot, ultroid_cmd
from ._inline import something


@ultroid_cmd(pattern="اضف مميز( (.*)|$)")
async def an(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    wt = await e.get_reply_message()
    if not (wt and wrd):
        return await e.eor(get_string("snip_1"))
    if "$" in wrd:
        wrd = wrd.replace("$", "")
    btn = format_btn(wt.buttons) if wt.buttons else None
    if wt and wt.media:
        wut = mediainfo(wt.media)
        if wut.startswith(("pic", "gif")):
            dl = await wt.download_media()
            variable = uf(dl)
            os.remove(dl)
            m = f"https://graph.org{variable[0]}"
        elif wut == "video":
            if wt.media.document.size > 8 * 1000 * 1000:
                return await e.eor(get_string("com_4"), time=5)
            dl = await wt.download_media()
            variable = uf(dl)
            os.remove(dl)
            m = f"https://graph.org{variable[0]}"
        else:
            m = pack_bot_file_id(wt.media)
        if wt.text:
            txt = wt.text
            if not btn:
                txt, btn = get_msg_button(wt.text)
            add_snip(wrd, txt, m, btn)
        else:
            add_snip(wrd, None, m, btn)
    else:
        txt = wt.text
        if not btn:
            txt, btn = get_msg_button(wt.text)
        add_snip(wrd, txt, None, btn)
    await e.eor(f"تم : إضافته مميز `${wrd}` وتم الحفظ 🧸♥️.")
    ultroid_bot.add_handler(add_snips, events.NewMessage())


@ultroid_cmd(pattern="مسح مميز( (.*)|$)")
async def rs(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    if not wrd:
        return await e.eor(get_string("snip_2"))
    if wrd.startswith("$"):
        wrd = wrd.replace("$", "")
    rem_snip(wrd)
    await e.eor(f"تم : مسح المميز `${wrd}` ♥️🧸.")


@ultroid_cmd(pattern="listsnip")
async def lsnote(e):
    if x := list_snip():
        sd = "SNIPS Found :\n\n"
        await e.eor(sd + x)
    else:
        await e.eor("لا يوجد مميزين هنا 🧸♥️")


async def add_snips(e):
    if not e.out and e.sender_id not in sudoers():
        return
    xx = [z.replace("$", "") for z in e.text.lower().split() if z.startswith("$")]
    for z in xx:
        if k := get_snips(z):
            msg = k["msg"]
            media = k["media"]
            rep = await e.get_reply_message()
            if rep:
                if k.get("button"):
                    btn = create_tl_btn(k["button"])
                    return await something(rep, msg, media, btn)
                await rep.reply(msg, file=media)
            else:
                await e.delete()
                if k.get("button"):
                    btn = create_tl_btn(k["button"])
                    return await something(e, msg, media, btn, reply=None)
                await ultroid_bot.send_message(e.chat_id, msg, file=media)


if udB.get_key("SNIP"):
    ultroid_bot.add_handler(add_snips, events.NewMessage())
