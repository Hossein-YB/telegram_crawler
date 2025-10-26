from peewee import (SqliteDatabase, Model, BigIntegerField, BooleanField, DateTimeField, ForeignKeyField, IntegerField, \
                    CharField, TextField)
import datetime

database = SqliteDatabase('telegram_crawler.db')


class BaseModel(Model):
    class Meta:
        database = database


class AdminsTBL(BaseModel):
    """Administrators and sudo users of the bot"""
    user_id = BigIntegerField(unique=True)
    is_sudo = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def insert_admin(cls, user_id: int, is_sudo: bool = False, is_active: bool = True) -> "AdminsTBL":
        return cls.get_or_create(user_id=user_id, is_sudo=is_sudo, is_active=is_active, )


class ChatsTBL(BaseModel):
    """Channels and groups monitored for crawling"""
    chat_id = BigIntegerField(unique=True)
    added_by = ForeignKeyField(AdminsTBL, backref='added_chats')

    realtime_crawl = BooleanField(default=False)
    crawl_old_messages = BooleanField(default=False)

    last_crawled_message_id = BigIntegerField(null=True)
    oldest_crawled_message_id = BigIntegerField(null=True)
    last_crawl_time = DateTimeField(null=True)
    total_crawled_messages = IntegerField(default=0)

    destination_chat_id = BigIntegerField(null=True)
    delay_between_messages = IntegerField(default=3)

    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)


class TargetUsersTBL(BaseModel):
    """Target users to track across all chats"""
    user_id = BigIntegerField(unique=True)
    track_messages = BooleanField(default=True)
    added_by = ForeignKeyField(AdminsTBL, backref='tracked_users')
    is_active = BooleanField(default=True)

    destination_chat_id = BigIntegerField(null=True)
    delay_between_messages = IntegerField(default=3)

    created_at = DateTimeField(default=datetime.datetime.now)


class WordsListTBL(BaseModel):
    """Keyword lists for message filtering"""
    list_words = TextField()
    is_check = BooleanField(default=True)
    created_by = ForeignKeyField(AdminsTBL, backref='word_lists')
    created_at = DateTimeField(default=datetime.datetime.now)


class CrawlScheduleTBL(BaseModel):
    """Automated crawling scheduling"""
    chat = ForeignKeyField(ChatsTBL, backref='schedules')
    schedule_type = CharField(choices=[
        ('realtime', 'Realtime'),
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly')
    ])
    interval_minutes = IntegerField(null=True)
    next_run = DateTimeField()
    is_active = BooleanField(default=True)


class BotSettingsTBL(BaseModel):
    """Global bot configuration settings"""
    key = CharField(unique=True)
    value = TextField()
    description = TextField(null=True)
