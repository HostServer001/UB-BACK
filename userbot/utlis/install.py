import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from userbot import *
from userbot.user import *
#from userbot.helpers import *
from userbot.config import *
from userbobot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from hellbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userbot.utils

        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Importing plugins...")
        LOGS.info("Bot - Successfully imported " + shortname)
    else:
        import userbot.utils

        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = user
        mod.user = user
        mod.HellBot = Userbo
        mod.tbot = Userbot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = userbot.utils
        mod.Config = Config
        mod.borg = bot
        mod.userbot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_bot = delete_bot
        mod.eod = delete_bot
        mod.Var = Config
        mod.admin_cmd = admin_cmd
       # mod.hell_cmd = hell_cmd
        mod.sudo_cmd = sudo_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = userbot.utils
        sys.modules["userbot"] = userbot
        # support for paperplaneextended
        sys.modules["userbot.events"] = userbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["userbot.plugins." + shortname] = mod
        LOGS.info("✅ Bot  - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"userbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

