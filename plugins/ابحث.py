# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• {i}بحث عن صورة <search query> ; <no of pics>
    البحث عن الصور.
"""

from pyUltroid.fns.misc import unsplashsearch

from . import asyncio, download_file, get_string, os, ultroid_cmd


@ultroid_cmd(pattern="بحث عن صورة( (.*)|$)")
async def searchunsl(ult):
    match = ult.pattern_match.group(1).strip()
    if not match:
        return await ult.eor("أعطني شيئا للبحث 🧸♥️")
    num = 5
    if ";" in match:
        num = int(match.split(";")[1])
        match = match.split(";")[0]
    tep = await ult.eor(get_string("com_1"))
    res = await unsplashsearch(match, limit=num)
    if not res:
        return await ult.eor(get_string("unspl_1"), time=5)
    CL = [download_file(rp, f"{match}-{e}.png") for e, rp in enumerate(res)]
    imgs = [z for z in (await asyncio.gather(*CL)) if z]
    await ult.client.send_file(
        ult.chat_id, imgs, caption=f"تم الرفع {len(imgs)} الصور!"
    )
    await tep.delete()
    [os.remove(img) for img in imgs]
