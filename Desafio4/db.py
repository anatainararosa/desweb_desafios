import sys
import mariadb


def connect():
    try:
        connection = mariadb.connect(
            user="root",
            password="123456",
            host="127.0.0.1",
            port=3306,
            database = "desafiodw"
        )
        connection.auto_reconnect = True
        connection.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)
    return connection