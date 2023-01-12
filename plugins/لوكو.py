# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}لوكو <text>`
   قم بإنشاء شعار للنص المحدد
   أو الرد على الصورة ، لكتابة النص الخاص بك عليها.
   أو الرد على ملف الخط ، للكتابة بهذا الخط.

"""
import glob
import os
import random

from telethon.tl.types import InputMessagesFilterPhotos

from pyUltroid.fns.misc import unsplashsearch
from pyUltroid.fns.tools import LogoHelper

from . import OWNER_ID, OWNER_NAME, download_file, get_string, mediainfo, ultroid_cmd


@ultroid_cmd(pattern="لوكو( (.*)|$)")
async def logo_gen(event):
    xx = await event.eor(get_string("com_1"))
    name = event.pattern_match.group(1).strip()
    if not name:
        return await xx.eor("`أعط اسما أيضا 🧸 ♥ ️!`", time=5)
    bg_, font_ = None, None
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document") and (
                ("font" in temp.file.mime_type)
                or (".ttf" in temp.file.name)
                or (".otf" in temp.file.name)
            ):
                font_ = await temp.download_media("resources/fonts/")
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    if not bg_:
        if event.client._bot:
            SRCH = ["blur background", "background", "neon lights", "wallpaper"]
            res = await unsplashsearch(random.choice(SRCH), limit=1)
            bg_ = await download_file(res[0], "resources/downloads/logo.png")
        else:
            pics = []
            async for i in event.client.iter_messages(
                "@Tepthone", filter=InputMessagesFilterPhotos
            ):
                pics.append(i)
            id_ = random.choice(pics)
            bg_ = await id_.download_media()

    if not font_:
        fpath_ = glob.glob("resources/fonts/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        strke = 10
    elif len(name) >= 9:
        strke = 5
    else:
        strke = 20
    name = LogoHelper.make_logo(
        bg_,
        name,
        font_,
        fill="white",
        stroke_width=strke,
        stroke_fill="black",
    )
    await xx.edit("`Done!`")
    await event.client.send_file(
        event.chat_id,
        file=name,
        caption=f"الوكو من [{OWNER_NAME}](tg://user?id={OWNER_ID})",
        force_document=True,
    )
    os.remove(name)
    await xx.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
