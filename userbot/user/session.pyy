import sys

from telethon import TelegramClient

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

from telethon.sessions import StringSession

from hellbot.config import Config

if Config.SESSION:

    session = StringSession(str(Config.SESSION))

else:

    session = "user"

try:

    user = TelegramClient(

        session=session,

        api_id=Config.APP_ID,

        api_hash=Config.API_HASH,

        connection=ConnectionTcpAbridged,

        auto_reconnect=True,

        connection_retries=None,

    )

except Exception as e:

    print(f"Error SESSION - {e}")

    sys.exit()
