# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ الأوامر المتاحة -

• `{i}اضف ملاحظة <word><reply to a message>`
    أضف ملاحظة في الدردشة المستخدمة مع الرسالة التي تم الرد عليها واختيار الكلمة.

• `{i}حذف ملاحظة <word>`
    حذف الملاحظة في المحادثة.

• `{i}قائمة الملاحظات`
    قائمة بجميع الملاحظات ♥ ️🧸.

• Use :
   set notes in group so all can use it.
   type `#(Keyword of note)` to get it
"""
import os

from telegraph import upload_file as uf
from telethon.utils import pack_bot_file_id

from pyUltroid.dB.notes_db import add_note, get_notes, list_note, rem_note
from pyUltroid.fns.tools import create_tl_btn, format_btn, get_msg_button

from . import events, get_string, mediainfo, udB, ultroid_bot, ultroid_cmd
from ._inline import something


@ultroid_cmd(pattern="اضف ملاحظة( (.*)|$)", admins_only=True)
async def an(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    wt = await e.get_reply_message()
    chat = e.chat_id
    if not (wt and wrd):
        return await e.eor(get_string("notes_1"), time=5)
    if "#" in wrd:
        wrd = wrd.replace("#", "")
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
            add_note(chat, wrd, txt, m, btn)
        else:
            add_note(chat, wrd, None, m, btn)
    else:
        txt = wt.text
        if not btn:
            txt, btn = get_msg_button(wt.text)
        add_note(chat, wrd, txt, None, btn)
    await e.eor(get_string("notes_2").format(wrd))
    ultroid_bot.add_handler(notes, events.NewMessage())


@ultroid_cmd(pattern="حذف ملاحظة( (.*)|$)", admins_only=True)
async def rn(e):
    wrd = (e.pattern_match.group(1).strip()).lower()
    chat = e.chat_id
    if not wrd:
        return await e.eor(get_string("notes_3"), time=5)
    if wrd.startswith("#"):
        wrd = wrd.replace("#", "")
    rem_note(int(chat), wrd)
    await e.eor(f"تم حذف: `#{wrd}` الملاحظة.")


@ultroid_cmd(pattern="قائمة الملاحظات$", admins_only=True)
async def lsnote(e):
    if x := list_note(e.chat_id):
        sd = "الملاحظات الموجودة في هذه الدردشات ♥️🧸\n\n"
        return await e.eor(sd + x)
    await e.eor(get_string("notes_5"))


async def notes(e):
    xx = [z.replace("#", "") for z in e.text.lower().split() if z.startswith("#")]
    for word in xx:
        if k := get_notes(e.chat_id, word):
            msg = k["msg"]
            media = k["media"]
            if k.get("button"):
                btn = create_tl_btn(k["button"])
                return await something(e, msg, media, btn)
            await e.client.send_message(
                e.chat_id, msg, file=media, reply_to=e.reply_to_msg_id or e.id
            )


if udB.get_key("NOTE"):
    ultroid_bot.add_handler(notes, events.NewMessage())
