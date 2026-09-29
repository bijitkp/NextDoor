from config.config import settings
from database.database import Database


db = Database(settings.auth_db_name)