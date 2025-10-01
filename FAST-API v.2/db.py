import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = "database-2.cm1sg6s2un1d.us-east-1.rds.amazonaws.com"
DB_NAME = "test"
DB_USER = "postgres"
DB_PASS = "Uide.asu.123"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        cursor_factory=RealDictCursor
    )
