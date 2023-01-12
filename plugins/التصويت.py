# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}poll <question> ; <option> ; <option>`
    Get the Anonymous Poll with Given Options

• `{i}poll <question> ; <option> ; <option> | <type>`
    Get the poll specified with desired type!
    type should be any of  `public`,  `multiple` or `quiz`

• `{i}poll <question> ; <option> ; <option> | quiz_<answerno>`
    Get the quiz poll where answerno is the number of option which is correct

"""
from telethon.tl.types import InputMediaPoll, Poll, PollAnswer

from . import get_string, ultroid_cmd


@ultroid_cmd(
    pattern="تصويت( (.*)|$)",
)
async def uri_poll(e):
    if not e.client._bot and e.is_private:
        return await e.eor("`استخدم هذا في المجموعة / القناة.`", time=15)
    match = e.pattern_match.group(1).strip()
    if not match:
        return await e.eor("`إعطاء المدخلات المناسبة...`", time=5)
    if ";" not in match:
        return await e.eor("`تعذر تحديد الخيارات ❤️🧸.`.", time=5)
    ques = match.split(";")[0]
    option = match.split(";")[1::]
    publ = None
    quizo = None
    karzo = None
    mpp = None
    if "|" in match:
        ptype = match.split(" | ")[1]
        option = match.split("|")[0].split(";")[1::]
        if "_" in ptype:
            karzo = [str(int(ptype.split("_")[1]) - 1).encode()]
            ptype = ptype.split("_")[0]
        if ptype not in ["public", "quiz", "multiple"]:
            return await e.eor("`نوع الاستطلاع غير صالح ♥ ️🧸...`", time=5)
        if ptype == "multiple":
            mpp = True
        elif ptype == "public":
            publ = True
        elif ptype == "quiz":
            quizo = True
    if len(option) <= 1:
        return await e.eor("`يجب أن تكون الخيارات أكثر من 1..`", time=5)
    m = await e.eor(get_string("com_1"))
    OUT = [PollAnswer(option[on], str(on).encode()) for on in range(len(option))]
    await e.client.send_file(
        e.chat_id,
        InputMediaPoll(
            Poll(20, ques, OUT, multiple_choice=mpp, public_voters=publ, quiz=quizo),
            correct_answers=karzo,
        ),
    )
    await m.delete()
