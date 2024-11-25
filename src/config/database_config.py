from pymysql import connect
class DatabaseConfig:

    @staticmethod
    def getConnection():
        host: str = 'localhost'
        port: int = 3306
        user: str = 'root'
        password: str = '0520'
        database: str = 'pymysql_study'

        return connect(host=host, port=port, user=user, password=password, database=database)