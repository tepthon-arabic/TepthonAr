from plugins import ultroid_bot
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import asyncio
from telethon import events
c = requests.session()
bot_username = '@zmmbot'
plugins = ['yes']


@ultroid_bot.on(pattern="تجميع المليار$")
async def _(event):
    if plugins[0] == "yes":
        await event.edit("᯽︙سيتم تجميع النقاط , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء")
        channel_entity = await ultroid_bot.get_entity(bot_username)
        await ultroid_bot.send_message('@t06bot', '/start')
        await asyncio.sleep(5)
        msg0 = await ultroid_bot.get_messages('@t06bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await ultroid_bot.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if plugins[0] == 'no':
                break
            await asyncio.sleep(5)

            list = await ultroid_bot(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
