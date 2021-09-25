#sqlite3 연습

import sqlite3

#sql db 불러오기
conn = sqlite3.connect('./requests_1/SQLite/SqlDDL.db')

#cursor 생성
cur = conn.cursor()

#SQL 명령어 작성

CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Item(
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null
    );
"""

#SQL 명령 실행
cur.execute(CREATE_SQL)

#데이터베이스 닫기
conn.close()