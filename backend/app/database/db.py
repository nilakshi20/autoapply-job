from urllib.parse import quote_plus
from sqlalchemy import create_engine
from app.config.settings import settings

password = quote_plus(settings.POSTGRES_PASSWORD)

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{password}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(
    DATABASE_URL,
    echo=settings.DEBUG
)