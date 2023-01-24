# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **سورس تيبثون العربي** •\n
• قناة السورس - [Click Here](https://t.me/Tepthon)
• المطور - [Click Here](https://t.me/PPF22)
• كروب الدعم 🔧 - @Tepthon_Help
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://t.me/Tepthon"),
        Button.url("المطور ♥️", "https://t.me/PPF22"),
    ],
    [Button.url("كروب المساعدة 🛠️", "t.me/Tepthon_Help")],
]

ULTSTRING = """🎇 **شكرًا على تنصيب سورس تيبثون العربي!**

• فيما يلي بعض العناصر الأساسية ، حيث يمكنك معرفة استخدامها."""


@ultroid_cmd(
    pattern="قناة السورس$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"خطأ أثناء أمر الريبو : {str(er)}")
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="تيبثون$")
async def useUltroid(rs):
    button = Button.inline("البدء >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://graph.org/file/c0c898f1370417fbfc018.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[اضغط هنا]({msg.message_link})**")
