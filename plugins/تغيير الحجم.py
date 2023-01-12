# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

•`{i}size <reply to media>`
   To get size of it.

•`{i}resize <number> <number>`
   To resize image on x, y axis.
   eg. `{i}resize 690 960`
"""
from PIL import Image

from . import HNDLR, eor, get_string, os, ultroid_cmd


@ultroid_cmd(pattern="الحجم$")
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await e.eor(get_string("ascii_1"))
    k = await e.eor(get_string("com_1"))
    if hasattr(r.media, "document"):
        img = await e.client.download_media(r, thumb=-1)
    else:
        img = await r.download_media()
    im = Image.open(img)
    x, y = im.size
    await k.edit(f"أبعاد هذه الصورة 🧸♥️\n`{x} x {y}`")
    os.remove(img)


@ultroid_cmd(pattern="تغيير الحجم( (.*)|$)")
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await e.eor(get_string("ascii_1"))
    sz = e.pattern_match.group(1).strip()
    if not sz:
        return await eor(
            f"إعطاء بعض الحجم لتغيير الحجم ، مثل `{HNDLR}تغيير الحجم 720 1080` ", time=5
        )
    k = await e.eor(get_string("com_1"))
    if hasattr(r.media, "document"):
        img = await e.client.download_media(r, thumb=-1)
    else:
        img = await r.download_media()
    sz = sz.split()
    if len(sz) != 2:
        return await eor(
            k, f"إعطاء بعض الحجم لتغيير الحجم ، مثل `{HNDLR}تغيير الحجم 720 1080` ", time=5
        )
    x, y = int(sz[0]), int(sz[1])
    im = Image.open(img)
    ok = im.resize((x, y))
    ok.save(img, format="PNG", optimize=True)
    await e.reply(file=img)
    os.remove(img)
    await k.delete()
