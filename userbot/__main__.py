import glob

import os

import sys

from pathlib import Path

import telethon.utils

from telethon import TelegramClient

from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from telethon.tl.functions.messages import ImportChatInviteRequest

from userbot import LOGS, bot, tbot

from userbot.user.session import user

from userbot.config import Config

from userbot.utils import load_module

from userbot.version import __user__ as botver

hl = Config.HANDLER

USER_PIC = "https://telegra.ph/file/cb0bd62632a3a2b6b2726.jpg"

# let's get the bot ready

async def h1(bot_token):

    try:

        await bot.start(bot_token)

        bot.me = await bot.get_me()

        bot.uid = telethon.utils.get_peer_id(bot.me)

    except Exception as e:

        LOGS.error(f"Error SESSION - {str(e)}")

        sys.exit()

# Multi-Client helper

async def user_client(client):

    client.me = await client.get_me()

    client.uid = telethon.utils.get_peer_id(client.me)

# hellbot starter...

if len(sys.argv) not in (1, 3, 4):

    bot.disconnect()

else:

    bot.tgbot = None

    try:

        if Config.BOT_USERNAME is not None:

            LOGS.info("Checking Telegram Bot Username...")

            bot.tgbot = tbot

            LOGS.info("Checking Completed. Proceeding to next step...")

            LOGS.info("✅ Starting Bot ✅")

            bot.loop.run_until_complete(h1(Config.BOT_USERNAME))

            failed_client = hells()

            global total

            total = 5 - failed_client

            LOGS.info("✅ Bot Startup Completed ✅")

            LOGS.info(f"» Total Clients = {total} «")

        else:

            bot.start()

            failed_client = hells()

            total = 5 - failed_client

#         LOGS.info(f"» Total Clients = {total} «")

    except Exception as e:

        LOGS.error(f"BOT_TOKEN - {str(e)}")

        sys.exit()

# imports plugins...

path = "userbot/plugins/*.py"

files = glob.glob(path)

for name in files:

    with open(name) as f:

        path1 = Path(f.name)

        shortname = path1.stem

        load_module(shortname.replace(".py", ""))

# let the party begin...

LOGS.info("Starting Bot Mode !")

tbot.start()

LOGS.info("✅ Your Bot Is Now Working ✅")

#LOGS.info("Head to @Its_HellBot for Updates. Also join chat group to get help regarding to HellBot.")

#LOGS.info(f"» Total Clients = {total} «")

# that's life...

async def hell_is_on():

    try:

        x = await bot.get_me()

        xid = telethon.utils.get_peer_id(x)

        send_to = Config.LOGGER_ID if Config.LOGGER_ID != 0 else xid

        await bot.send_file(

            send_to,

            HELL_PIC,

            caption=f"#Online \n Bot Online",

            parse_mode="HTML",

        )

    except Exception as e:

        LOGS.info(str(e))

bot.loop.create_task(hell_is_on())

if len(sys.argv) not in (1, 3, 4):

    bot.disconnect()

else:

    bot.tgbot = None

    bot.run_until_disconnected()

