#sqlite3 연습

import sqlite3

#sql db 불러오기
conn = sqlite3.connect('./requests_1/SQLite/SqlDDL.db')

#cursor 생성
cur = conn.cursor()

#SQL 명령어 작성

# -중복제거
# SELECT DISTINCT (컬럼명) FROM 테이블명


# -중복된 데이터 제거 후 COUNT
# SELECT COUNT(DISTINCT (컬럼명)) FROM 테이블명


# -중복찾기
# SELECT 컬럼명 FROM 테이블명 GROUP BY 컬럼명 HAVING COUNT (컬럼명) > 1


SELECT_SQL1 = """
    SELECT user.email,gender,age FROM board INNER JOIN user WHERE board.author = user.email; 
"""

# #SQL 명령 실행
cur.execute(SELECT_SQL1)

rows = cur.fetchall()
for row in rows:
    print(row)

#데이터베이스 닫기
conn.close()