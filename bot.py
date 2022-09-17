import os
import pyrogram

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config



if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "filter bot",
        bot_token='5569567626:AAG4fEKnv998AZcoNjdt0WTAPLW56r8UdHc',
        api_id='10651048',
        api_hash='37775aca7d11f450ecde375baac17fe7',
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(str(1323557247))
    app.run()
