import psycopg2

conn = psycopg2.connect(
    dbname='cinema_booking',
    user='cinema_user',
    password='booking',
    host='localhost',
    port='5432'
)

print("✅ PostgreSQL connected!")
