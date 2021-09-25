#sqlite3 연습

import sqlite3

#sql db 불러오기
conn = sqlite3.connect('./requests_1/SQLite/SqlDDL.db')

#cursor 생성
cur = conn.cursor()

#SQL 명령어 작성

INSERT_SQL = """
    INSERT INTO Item(code,name,price) VALUES (?,?,?);
"""
DELETE_SQL = """
    DELETE FROM Item;
"""
#cur.execute(DELETE_SQL)

data = (
    ('A02','무선기계식키보드', 89000),
    ('A03','커브드모니터', 289000),
    ('A04','블루투스스피커', 29000)
)



# #SQL 명령 실행
cur.execute(INSERT_SQL,('A01','무선게이밍마우스',48000))
#여러개 할때
cur.executemany(INSERT_SQL,data)

#commit INSERT, UPDATE, DELETE는 commit 해야 실제로 반영됨
conn.commit()

#데이터베이스 닫기
conn.close()