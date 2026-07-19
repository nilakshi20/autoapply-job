from sqlalchemy import text
from app.database.db import engine
from app.database.db import DATABASE_URL



try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("✅ Database Connected Successfully!")
        print(result.scalar())
except Exception as e:
    print("❌ Database Connection Failed!")
    print(e)

    print(DATABASE_URL)