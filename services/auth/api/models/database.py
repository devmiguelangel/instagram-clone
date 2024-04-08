from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from api.config.settings import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()
