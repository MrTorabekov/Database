# import psycopg2
#
# conn = psycopg2.connect(database="users",
#                         user="postgres",
#                         password=1,
#                         host="localhost",
#                         port=5432)
#
# cursor = conn.cursor()  # creating a cursor
# cursor.execute("""select * from users""")
# for row in cursor.fetchall():
#     print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}")
#
# conn.commit()
# conn.close()



import psycopg2
from colorama import Fore


def create_connection():
    try:
        conn = psycopg2.connect(database='users', user='postgres', password='1', port='5432', host='localhost')
        cursor = conn.cursor()
        print(Fore.LIGHTRED_EX + "Database connect successfully")
        cursor.execute("""CREATE TABLE IF NOT EXISTS admin(
         id serial PRIMARY KEY,
         name varchar(100) NOT NULL,
         username varchar(100) NOT NULL UNIQUE) """)
        conn.commit()
        print(Fore.LIGHTGREEN_EX + "Table created successfully")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_connection()