# btn : about and close change here

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id=5743248220'>अजनबी</a>\n○ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Animes_Station'>ANIME STATION</a>\n○ ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ : <a href='https://t.me/ongoing_anime_station'>ONGOING ANIME STATION</a>\n○ ᴄʜᴀᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/Anime_talk_station'>Chat</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                        InlineKeyboardButton('🖇 ᴍᴜsᴛ Jᴏɪɴ', url='https://t.me/Animes_Station')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
