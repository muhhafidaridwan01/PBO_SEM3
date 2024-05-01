import psycopg2

class DBConnection:

    def __init__(self):
        self.host = 'pg-15a3c0b7-hafidaridwan25-c2ef.c.aivencloud.com'
        self.port = 20549
        self.name = 'defaultdb' # nama database
        self.user = 'avnadmin'
        self.password = 'AVNS_F9xSJQ-VQUj2GjXw0uG'
        self.ca_file = 'ca.pem'  # Path to your ca.pem file
        self.connection_timeout = 20
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()
        
    @property
    def connection_status(self):
        return self.connected
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(host=self.host,
                                        port=self.port,
                                        database=self.name,
                                        user=self.user,
                                        password=self.password,
                                        sslmode='require',  # To enforce SSL
                                        sslrootcert=self.ca_file,
                                        connect_timeout=self.connection_timeout)  # Connection timeout)
            self.cursor = self.conn.cursor()
            self.connected = True
        except psycopg2.Error as e:
            self.connected = False
            print("Error connecting to the database:", e)
        return self.conn

    def disconnect(self):
        if self.connected:
            self.conn.close()
            self.connected = False
        else:
            self.conn = None

    def findOne(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    def findAll(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def insert(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def update(self, sql, val):
        self.connect()
        self.cursor.execute(sql, val)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def delete(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.conn.commit()
        self.affected = self.cursor.rowcount        
        return self.affected

    def show(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.result = self.cursor.fetchone()
        return self.result

    @property
    def info(self):
        if self.connected:
            return "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."
        
A = DBConnection()
B = A.info
print(B)