from plugins import ultroid_cmd


@ultroid_cmd(pattern="الاوامر")
async def hi(event):
    await edit_or_reply(
        eventually, 
        """[ . 𝐑𝐄𝐏𝐓𝐇𝐎𝐍𓌶 - 𝐂𝐌𝐃- .](t.me/Repthon)\n 𓅔 ━━━━━ ━━—×—━━ ━━━━━ 𓅔\n\n - آهـلاً وسـهلاً بك فـي قائـمة أوامـر السـورس [Click here|اضغـط هنـا](https://graph.org/قائمة-اوامر-ريبثون-01-10)\n\n"""
        link_preview=False,
    )
