# By - The LΣGΣΠD
import asyncio
from userbot.utils import admin_cmd 
 
 
 
 
@borg.on(admin_cmd(pattern="masthurbet")) 
 
 
 
async def masthurbet(event):
 
 
 
    muth = await event.edit("Masthurbet..! 🤤✊💦")
    await asyncio.sleep(2)
    await muth.delete()
    await event.client.send_file(
        event.chat_id, "CAADAQADUAIAApp2KUXzdNtNEG6pRgI"
    )
