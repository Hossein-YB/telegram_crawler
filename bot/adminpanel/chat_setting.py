from typing import TYPE_CHECKING

from pyrogram.enums import ChatType

if TYPE_CHECKING:
    from bot import CBot
from pyrogram.types import Message


chat_types = [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]


class ChatSetting:
    async def get_all_chat(self: "CBot", clt, msg: Message):
        """Send the names and IDs of robot groups and channels"""
        t = ""
        async for dialog in self.get_dialogs():
            if dialog.chat.type in chat_types:
                t += f"{dialog.chat.title[:9]} > `{dialog.chat.id}`\n"
        return await msg.reply(t)

    async def add_new_chat(self: "CBot", clt, msg: Message):
        await self.ask()
        pass
