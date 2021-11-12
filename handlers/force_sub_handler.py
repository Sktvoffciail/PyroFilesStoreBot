# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def handle_force_sub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="🚫 Sorry Sir Or Bro, You are Banned to use me. Contact my [Support Group](https://t.me/Sk_Tv_Group)🚫",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**⚠️ Sorry Sir Your Not Subscribed Our Premium Membership Plan So Please Subscribe First And Use Me ⚠️**\n\n"
                 "⚠️ மன்னிக்கவும் நீங்கள் எங்கள் பிரீமியம் உறுப்பினர் திட்டத்திற்கு குழுசேரவில்லை எனவே முதலில் குழுசேர்ந்து பிறகு என்னை பயன்படுத்தவும் ⚠️ ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💸 Buy Premium Membership 💸", url="https://t.me/Sk8903")
                    ],
                    [
                        InlineKeyboardButton("⭕ I Buyed Premium Membership ⭕", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/Sk_Tv_Group).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
