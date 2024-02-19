import mysql.connector


class DatabaseConnection:
    _instance = None

    def __new__(cls, host, user, password, database):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Connection established only once during the first instantiation
            try:
                cls._connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
                cls._cursor = cls._connection.cursor(dictionary=True)
                print(f'Database connected at {host}')
            except mysql.connector.Error as e:
                raise ConnectionError(
                    f'Could not connect to database: {str(e)}')
        return cls._instance

    @property
    def cursor(self):
        return self._cursor

    @property
    def connection(self):
        return self._connection

    def commit(self):
        self._connection.commit()

    def close(self):
        self._cursor.close()
        self._connection.close()
        DatabaseConnection._instance = None
