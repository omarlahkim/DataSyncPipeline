import sqlite3

class DatabaseEngine:
    def __init__(self):
        self.__db = 'data.db'
        self.__database = self.connect(self.__db)
        self.__cursor = self.__database.cursor()
        pass
    def connect(self,database):
        return sqlite3.connect(database)
    # Create table
    def createTables(self):
        self.__cursor.execute("CREATE TABLE mgroup (gid TEXT PRIMARY KEY)")
        self.__cursor.execute("CREATE TABLE user (uid TEXT PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, lastpswdchange TEXT, minimum TEXT, maximum TEXT, warn TEXT, inactive TEXT, expire TEXT, shell TEXT, homedir TEXT, gecos TEXT, gid TEXT, FOREIGN KEY (gid) REFERENCES mgroup (gid) ON DELETE CASCADE ON UPDATE NO ACTION)")
#Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)
    def insertData(self,uid,username,password,gecos, homedir, shell, lastpasschange, minimum, maximum, warn, inactive, expire, gid):
        self.__cursor.execute("INSERT OR IGNORE INTO mgroup (gid) VALUES(?);",[str(gid)])
        self.__cursor.execute("INSERT INTO user (uid,username,password,gecos, homedir, shell, lastpswdchange, minimum, maximum, warn, inactive, expire, gid) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?);", [str(uid),str(username),str(password),str(lastpasschange), str(minimum), str(maximum), str(warn), str(inactive), str(expire),str(shell), str(homedir), str(gecos), str(gid)])
        self.__database.commit()

    def visualizeDate(self):
        print(self.__cursor.execute("SELECT * FROM mgroup;"))
#D = DatabaseEngine()
#D.createTables()
#D.insertData()
#D.visualizeDate()
