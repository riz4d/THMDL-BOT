from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import api_hash,api_id,bot_token
from constant import url
import wget
import requests
import os


app = Client(
    "THM-DL-BOT",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
@app.on_message(filters.command('start'))
async def echo(client,message):
    await message.reply('Hey Dude\nHow are you??\n\nSent me a TryHackMe Certificate Number I will validate it for you and also sent you to a copy\n\nEg : `THM-UL7X2KN6EU`',
                        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Developer', url='https://t.me/riz4d')
                ]
            ]
        )
                        )
@app.on_message(filters.text & filters.private)
async def echo(client, message):
    certificate_no = message.text
    cerdl = url+certificate_no+'.png'
    req = requests.get(cerdl)
    status=req.status_code
    dl=''
    
    if str(status)=='200':
        await message.reply('Congragulations! \n\n`'+certificate_no+'` Is a Valid Certificate, Issued by TryHackMe')
        file=wget.download(cerdl)
        await message.reply_photo(file)
    else:
        await message.reply("Sorry It's a Invalid")
    os.remove(file)
    print(message.text)


app.run()
