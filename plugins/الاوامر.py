from plugins import ultroid_cmd
from telethon import functions, types,events

HMD = """[ . 𝐓𝐄𝐏𝐇𝐎𝐍 - 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 ♛ .](t.me/Tepthone)\n 𓅔━ ━━━━✓━ 𓅔\n\n - آهـلاً وسـهلاً بك فـي قائـمة أوامـر السـورس [Click here|اضغـط هنـا](https://graph.org/%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%B3%D9%88%D8%B1%D8%B3-%D8%AA%D9%8A%D8%A8%D8%AB%D9%88%D9%86-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A-01-11)\n\n"""


@ultroid_cmd(pattern="الاوامر")
async def hi(event):
    await event.edit(f"{HMD}")
