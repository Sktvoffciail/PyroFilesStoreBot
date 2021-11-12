# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	FEATURES = f"""
⚡ Features FEATURES

💖 DIRECT TELEGRAM VIDEO (Newly Re Telecast Serials + Ullam Kollai Poguthada Season 2)

💖 NO WATERMARK 

💖 24 HRS CHAT SUPPORT

💖 ALL QUALITIES (Ullam Kollai Poguthada Season 2 Only)

💖 ULLAM KOLLAI POGUTHADA SEASON 2 NEW EPISODES

💖 EXTRA......

‼️ ** More Help : ** @Sk8903
"""
	ABOUT_DEV_TEXT = f"""
💝 **My God ** @Sk8903

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

`spkarnan81@okaxis` (Upi Id)
"""
	HOME_TEXT = """
வணக்கம் 🖐️ [{}](tg://user?id={})\n\n என்னை நீங்கள் சீரியல்கள் பார்க்க பயன்படுத்தி கொள்ளலாம்.

⚡ என்னை உருவாக்க என்னுடைய கடவுள் 💝 மிகவும் சிரமப்பட்டார் ஆகையால் உங்களால் முடிந்த உதவிகளை எங்களுக்கு செய்ய விரும்பினால் உடனே Donate செய்யுங்கள் ⚡

💖Upi Id : `spkarnan81@okaxis`
"""
