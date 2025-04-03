from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd

# Define database connection
DB_USER = "YOUR POSTGRES USER HERE"
DB_PASSWORD = "YOUR POSTGRES PASSWORD HERE"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "baseball_stats"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create database engine
engine = create_engine(DATABASE_URL)

# Define ORM Base
Base = declarative_base()

# Define Table Schema
class PlayerStats(Base):
    __tablename__ = "player_stats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    team = Column(String)
    plate_appearances = Column(Integer)
    home_runs = Column(Integer)
    batting_average = Column(Float)
    on_base_percentage = Column(Float)
    slugging_percentage = Column(Float)

# Create tables if they don’t exist
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

def load_data_to_postgres(df: pd.DataFrame):
    # Convert DataFrame to list of PlayerStats objects
    players = [
        PlayerStats(
            name=row["player_name"],
            team=row["team"],
            plate_appearances=row["plate_appearances"],
            home_runs=row["home_runs"],
            batting_average=row["batting_average"],
            on_base_percentage=row["on_base_percentage"],
            slugging_percentage=row["slugging_percentage"]
        )
        for _, row in df.iterrows()
    ]

    # Insert data using SQLAlchemy
    session.bulk_save_objects(players)
    session.commit()

    print("Data successfully saved to PostgreSQL.")

    # Close session
    session.close()
