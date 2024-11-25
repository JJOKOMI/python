from dataclasses import dataclass
from pymysql import cursors
from src.config.database_config import DatabaseConfig
from src.entity.user_entity import User

@dataclass
class UserRepositoryStudy:

  def insert(self, user: User):
    connection = DatabaseConfig.getConnection()
    cursor = connection.cursor()
    sql = '''
INSERT INTO user_tb
VALUES(default, %s, %s, %s, %s, now(), now())
'''
    insertCount = cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
    print(f"User 데이터 추가 성공 {insertCount}건")
    connection.commit()

  def findById(self, user_id: int):
    connection = DatabaseConfig.getConnection()
    cursor = connection.cursor(cursor=cursors.DictCursor)
    sql = '''
    SELECT * FROM user_tb WHERE user_id = %s
    '''
    cursor.execute(query=sql, args=(user_id, ))
    result = cursor.fetchall()
    print(result)