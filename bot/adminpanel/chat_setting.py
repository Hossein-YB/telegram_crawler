from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from bot import CBot
from pyrogram.types import Message


class ChatSetting:
    async def add_new_chat(self, clt, msg: Message):
        return await msg.reply(f"{msg.from_user.id}")