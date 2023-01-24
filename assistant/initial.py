# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **شكرًا على تنصيب سورس تيبثون العربي!**

• فيما يلي بعض العناصر الأساسية ، حيث يمكنك معرفة استخدامها.""",
    2: """🎉** معلومات عن تيبثون العربي**

🧿  تيبثون هو سورس تليثون يوزر بوت قوي وقابل للتوصيل ، مصنوع في بايثون من . يهدف إلى زيادة الأمان إلى جانب إضافة ميزات مفيدة أخرى.

❣ مشغل من **@Tepthon**""",
    3: """**💡• أسئلة وأجوبة •**

-> [مطور تيبثون](https://t.me/PPF22)

**• اعرف حول التحديثات**
  - انضم @tepthon.""",
    4: f"""• `اعرف جميع الاوامر المتاحه`

  - `{HNDLR}مساعدة`
  - `{HNDLR}الاوامر`""",
    5: """• **لأي استفسار أو اقتراح آخر**
  - الانتقال إلى **@tepthon_help**.

• شكرا للوصول حتى النهاية.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< رجوع", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("أبدا بالرجوع >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
