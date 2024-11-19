from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

DATABASE_URL = "postgresql://novo_sql_user:FjV5v83yvAfO8D4wJFla2zpVSze4Iz8M@dpg-cspti652ng1s7396pl9g-a.oregon-postgres.render.com/novo_sql"

engine = create_engine(
    DATABASE_URL, 
    #connect_args={"check_same_thread": False}  # SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("conexão feita")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        db.close()
