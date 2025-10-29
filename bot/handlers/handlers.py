from bot.convertions import MessageHandler
from pyrogram import filters
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from bot import CBot
from bot.handlers.handler_regex import *


class Handlers:
    def config_handlers(self: "CBot"):
        self.add_handler(MessageHandler(self.get_all_chat,
                                        (filters.sender_chat in self.admins or filters.me)
                                        and filters.regex(GET_ALL_CHATS)))

        self.add_handler(MessageHandler(self.add_new_chat,
                                        (filters.sender_chat in self.admins or filters.me)
                                        and filters.regex(ADD_NEW_CHAT)))
