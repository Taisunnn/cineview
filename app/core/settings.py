import os


class Settings:
    DATABASE_URI: str = (
        f"mysql+asyncmy://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{int(os.getenv('MYSQL_PORT'))}/{os.getenv('MYSQL_DATABASE')}"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"


settings = Settings()
