import os
from typing import Generator
import psycopg

passwordDB = os.getenv("SUPABASEPASSWORD")
print("SUPABASEPASSWORD:", passwordDB)  # <--- log temporal para ver si Vercel la ve

url = f"postgresql://postgres.llmoauphlyyhpjdlpuwa:{passwordDB}@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"
print("DB URL:", url)  # <--- log temporal

def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()

