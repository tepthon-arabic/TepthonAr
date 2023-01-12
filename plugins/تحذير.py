# Repthon - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/rogerpq/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available

•`{i}warn <reply to user> <reason>`
    Gives Warn.

•`{i}resetwarn <reply to user>`
    To reset All Warns.

•`{i}warns <reply to user>`
   To Get List of Warnings of a user.

•`{i}setwarn <warn count> | <ban/mute/kick>`
   Set Number in warn count for warnings
   After putting " | " mark put action like ban/mute/kick
   Its Default 3 kick
   Example : `setwarn 5 | mute`

"""

from pyUltroid.dB.warn_db import add_warn, reset_warn, warns

from . import eor, get_string, inline_mention, udB, ultroid_cmd


@ultroid_cmd(
    pattern="تحذير( (.*)|$)",
    manager=True,
    groups_only=True,
    admins_only=True,
)
async def warn(e):
    ultroid_bot = e.client
    reply = await e.get_reply_message()
    if len(e.text) > 5 and " " not in e.text[5]:
        return
    if reply:
        user = reply.sender_id
        reason = e.text[5:] if e.pattern_match.group(1).strip() else "unknown"
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await ultroid_bot.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("يرجى الرد على المستخدم أولًا.", time=5)
        try:
            reason = e.text.split(maxsplit=2)[-1]
        except BaseException:
            reason = "unknown"
    count, r = warns(e.chat_id, user)
    r = f"{r}|$|{reason}" if r else reason
    try:
        x = udB.get_key("SETWARN")
        number, action = int(x.split()[0]), x.split()[1]
    except BaseException:
        number, action = 3, "kick"
    if ("ban" or "kick" or "mute") not in action:
        action = "kick"
    if count + 1 >= number:
        if "ban" in action:
            try:
                await ultroid_bot.edit_permissions(e.chat_id, user, view_messages=False)
            except BaseException:
                return await e.eor("`حدث خطأً.`", time=5)
        elif "kick" in action:
            try:
                await ultroid_bot.kick_participant(e.chat_id, user)
            except BaseException:
                return await e.eor("`حدث خطأً.`", time=5)
        elif "mute" in action:
            try:
                await ultroid_bot.edit_permissions(
                    e.chat_id, user, until_date=None, send_messages=False
                )
            except BaseException:
                return await e.eor("`حدث خطأً.`", time=5)
        add_warn(e.chat_id, user, count + 1, r)
        c, r = warns(e.chat_id, user)
        ok = await ultroid_bot.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"المستخدم{user} تم تحذيره {action} بسبب {count+1} التحذيرات.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await e.eor(text)
        return reset_warn(e.chat_id, ok.id)
    add_warn(e.chat_id, user, count + 1, r)
    ok = await ultroid_bot.get_entity(user)
    user = inline_mention(ok)
    await eor(
        e,
        f"**WARNING :** {count+1}/{number}\n**To :**{user}\n**Be Careful !!!**\n\n**Reason** : {reason}",
    )


@ultroid_cmd(
    pattern="مسح التحذيرات( (.*)|$)",
    manager=True,
    groups_only=True,
    admins_only=True,
)
async def rwarn(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("يرجى الرد على المستخدم أولًا.")
    reset_warn(e.chat_id, user)
    ok = await e.client.get_entity(user)
    user = inline_mention(ok)
    await e.eor(f"تم مسح تحذيرات المستخدم {user}.")


@ultroid_cmd(
    pattern="التحذيرات( (.*)|$)",
    manager=True,
    groups_only=True,
    admins_only=True,
)
async def twarns(e):
    reply = await e.get_reply_message()
    if reply:
        user = reply.from_id.user_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await e.eor("يرجى الرد على مستخدم", time=5)
    c, r = warns(e.chat_id, user)
    if c and r:
        ok = await e.client.get_entity(user)
        user = inline_mention(ok)
        r = r.split("|$|")
        text = f"المستخدم {user} حذرته {c} التحذيرات.\n\n"
        for x in range(c):
            text += f"•**{x+1}.** {r[x]}\n"
        await e.eor(text)
    else:
        await e.eor("`No Warnings`")


@ultroid_cmd(pattern="ضع تحذير( (.*)|$)", manager=True)
async def warnset(e):
    ok = e.pattern_match.group(1).strip()
    if not ok:
        return await e.eor("stuff")
    if "|" in ok:
        try:
            number, action = int(ok.split()[0]), ok.split()[1]
        except BaseException:
            return await e.eor(get_string("schdl_2"), time=5)
        if ("ban" or "kick" or "mute") not in action:
            return await e.eor("`اختيار عقوبات التحذير mute / ban / kick option suported`", time=5)
        udB.set_key("SETWARN", f"{number} {action}")
        await e.eor(f"انتهيت من اختيار عقوبه التحذيرك {number} والعقوبه هو {action}")
    else:
        await e.eor(get_string("schdl_2"), time=5)
