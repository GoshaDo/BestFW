import sqlite3
from CONF import DB_FILE


def init_db(db_file):
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        list_of_tables = cur.execute("""SELECT tbl_name FROM sqlite_master WHERE type='table'
                                        AND tbl_name='searches'; """).fetchall()
        if len(list_of_tables) == 0:
            query = "create table searches(SEARCH TEXT,DATE TEXT,CHOSE_I int,"
            for i in range(8):
                if i != 7:
                    query += f"DAY_{i}_H int, DAY_{i}_U REAL, DAY_{i}_D REAL,"
                else:
                    query += f"DAY_{i}_H int, DAY_{i}_U REAL, DAY_{i}_D REAL)"
            cur.execute(query)


def insert_db(db_file, api):
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        query = f"INSERT INTO Searches VALUES(\'{api.location}\',julianday('now'),{api.op},"
        for i in range(8):
            if i != 7:
                query += f"{api.humidity[i]}, {api.max_temp[i]}, {api.min_temp[i]},"
            else:
                query += f"{api.humidity[i]}, {api.max_temp[i]}, {api.min_temp[i]})"
        print(query)
        cur.execute(query)


def show_db(db_file, table):
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        cur.execute(f"select * from {table}")
        print(cur.fetchall())


if __name__ == '__main__':
    init_db('weather.db')
    show_db(DB_FILE, 'Searches')
