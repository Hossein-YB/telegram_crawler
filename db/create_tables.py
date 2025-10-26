from db.models import (database, AdminsTBL, ChatsTBL, TargetUsersTBL, WordsListTBL, CrawlScheduleTBL, BotSettingsTBL)
from utils.settings import SODO_ID


def create_tables():
    """Create all database tables"""
    with database:
        database.create_tables([AdminsTBL, ChatsTBL, TargetUsersTBL, WordsListTBL, CrawlScheduleTBL, BotSettingsTBL])
    # insert sodo
    AdminsTBL.insert_admin(user_id=SODO_ID, is_sudo=True)
