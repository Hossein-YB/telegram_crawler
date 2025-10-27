from pyrogram import Client
from bot.handlers.handlers import Handlers
from bot.adminpanel.admin_panel import AdminPanel
from bot.utf8texts.texts import MessageTexts


class CBot(AdminPanel, Handlers, Client):
    def __init__(self, name: str, api_id, api_hash, **kwargs):
        self.text = MessageTexts()
        super().__init__(name=name, api_id=api_id, api_hash=api_hash, **kwargs)

    async def start(self):
        self.config_handlers()
        return await super().start()
