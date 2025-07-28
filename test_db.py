import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine, text
from decouple import config

def test_connection():
    try:
        DATABASE_URL = config("DATABASE_URL")
        engine = create_engine(DATABASE_URL)
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print("✅ Database connection successful!")
            print(f"PostgreSQL version: {version}")
            return True
    except Exception as e:
        print("❌ Database connection failed!")
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_connection()
