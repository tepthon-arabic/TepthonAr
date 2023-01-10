# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}تاك للكل`
    تاك لإفضل 100 عضو في المحادثة.

• `{i}تاك للأدمنية`
    تاك للأدمنية في المحادثة.

• `{i}تاك للمالك`
    تاك لمالك المحادثة

• `{i}تاك للبوتات`
    تاك لبوتات المحادثة.

• `{i}تاك للمتفاعلين`
    ضع علامة على الأعضاء النشطين مؤخرًا.

• `{i}تاك للمتصلين`
    تاك للأعضاء المتصلين(work only if privacy off).

• `{i}تاك للغير متصلين`
    تاك للأعضاء غير المتصلين(work only if privacy off).
"""

from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec

from . import inline_mention, ultroid_cmd


@ultroid_cmd(
    pattern="تاك(للمتصلين|للغير متصلين|للكل|للبوتات|للمتفاعلين|للأدمنية|للمالك)( (.*)|$)",
    groups_only=True,
)
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    o = 0
    nn = 0
    rece = 0
    xx = f"{lll}" if lll else ""
    lili = await e.client.get_participants(e.chat_id, limit=99)
    for bb in lili:
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o += 1
            if "للمتصلين" in okk:
                xx += f"\n{inline_mention(bb)}"
        elif isinstance(x, off):
            nn += 1
            if "للغير متصلين" in okk and not bb.bot and not bb.deleted:
                xx += f"\n{inline_mention(bb)}"
        elif isinstance(x, rec):
            rece += 1
            if "للمتفاعلين" in okk and not bb.bot and not bb.deleted:
                xx += f"\n{inline_mention(bb)}"
        if isinstance(y, owner):
            xx += f"\n꧁{inline_mention(bb)}꧂"
        if isinstance(y, admin) and "admin" in okk and not bb.deleted:
            xx += f"\n{inline_mention(bb)}"
        if "للكل" in okk and not bb.bot and not bb.deleted:
            xx += f"\n{inline_mention(bb)}"
        if "للبوتات" in okk and bb.bot:
            xx += f"\n{inline_mention(bb)}"
    await e.eor(xx)
#ترجمة_وتعريب_فريق_ريبثون
#ترجمة_حمد
#ترجمة_باقر
