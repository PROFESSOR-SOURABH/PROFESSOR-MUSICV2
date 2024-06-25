from pyrogram.types import InlineKeyboardButton

import config
from PROFESSOR import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="▪️sᴜᴘᴘᴏʀᴛ▪️", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ •",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="▪️sᴜᴘᴘᴏʀᴛ▪️", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="▪️ᴜᴘᴅᴀᴛᴇ▪️", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="🏩 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🏩", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
