import csv
import sqlite3


def insert_data_from_csv(db_file, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, "r", encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            cursor.execute(
                """INSERT INTO locations (name, category, address,
                 coordinates, offLeash, hours, outDoorSpace)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                row,
            )

    conn.commit()
    conn.close()


def create_tables(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS locations(
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        category TEXT,
                        address TEXT,
                        coordinates FLOAT,
                        offLeash INTEGER,
                        hours TEXT,
                        outDoorSpace INTEGER
                         )"""
    )

    # Create users tables
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        email TEXT UNIQUE,
                        password TEXT,
                        name TEXT,
                        username TEXT
                    )"""
    )

    # Create favorites table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS favourites (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        location_id INTEGER,
                        FOREIGN KEY(user_id) REFERENCES users(id),
                        FOREIGN KEY(location_id) REFERENCES locations(id)
                    )"""
    )

    conn.commit()
    conn.close()


def main():
    db_file = "C:\\Users\\victo\\OneDrive\\Desktop\\CST 8333 Assignment\\DogFriendly\\dogfriendly.sqlite3"
    # db_file = "C:\\Users\\ElmsJ\\Desktop\\DogFriendly\\dogfriendly.sqlite3"
    csv_file = "dogfriendly.csv"

    create_tables(db_file)
    insert_data_from_csv(db_file, csv_file)
    print("Data inserted successfully into SQLite database.")


if __name__ == "__main__":
    main()
