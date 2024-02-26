import os

class Settings:
    DATABASE_URI: str = f"mysql+asyncmy://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{int(os.getenv('MYSQL_PORT'))}/{os.getenv('MYSQL_DATABASE')}"

settings = Settings()
