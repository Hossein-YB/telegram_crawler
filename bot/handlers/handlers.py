from pyrogram.handlers import MessageHandler
from pyrogram import filters
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from bot import CBot


class Handlers:
    def config_handlers(self: "CBot"):
        self.add_handler(MessageHandler(self.add_new_chat,
                                        filters.me and filters.regex(r"^hi$")
                                        ))
