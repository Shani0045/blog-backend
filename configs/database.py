
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from sqlalchemy.ext.declarative import declarative_base

""""
class DBConfig:
    def __init__(self, config=None):
        self.user = os.getenv("PG_USER")
        self.password = os.getenv("PG_PASSWORD")
        self.host = os.getenv("PG_HOST")
        # self.port = os.getenv("PG_PORT")
        self.datsabase = os.getenv("PG_DATABASE")

        self.conn_string = f"postgresql://{self.user}:{self.password}@{self.host}/{self.database}"

    def create_engine_alchemy(self):
        self.engine = create_engine(
            self.conn_string, 
            echo = True, 
            pool_size = 2000,
            poolclass = QueuePool

         )
        return self.engine
    
    def get_db_session(self):
        self.session = sessionmaker(bind=self.create_engine_alchemy(), autocommit=False, autoflush=False)
        Base = declarative_base()

        db = self.session()
        try:
            yield db
        finally:
            db.close()

    """



SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:engineer@localhost/blogs"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        