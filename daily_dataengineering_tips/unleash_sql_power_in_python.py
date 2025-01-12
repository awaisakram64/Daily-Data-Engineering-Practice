from sqlalchemy import create_engine
from sqlalchemy import text

# Create an engine that connects to a SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)

# Execute a raw SQL query
def run_query():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'Hello, SQLAlchemy!' as greeting"))
        for row in result:
            print(row['greeting'])

run_query()