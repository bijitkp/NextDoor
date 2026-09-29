from config.config import settings
from database.database import Database


db = Database(settings.user_db_name)