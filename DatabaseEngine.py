import pymysql
import pymysql.cursors
import json

#TODO:
# Connect Remote Database
# Execute Queries on Remote Database
# ADD UPDATE case for Database
# https://www.freemysqlhosting.net/account/

class DatabaseEngine:
    def __init__(self):
        self.__config = json.load(open('config.json','r'))
        #self.__database = self.connect(self.__db)
        self.__database = pymysql.connect(host=self.__config['dbHost'],
                                     user=self.__config['dbUsername'],
                                     password=self.__config['dbPassword'],
                                     database=self.__config['dbName'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.__cursor = self.__database.cursor()
#Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)
    def truncateTable(self):
        self.__cursor.execute("TRUNCATE TABLE user;")
        self.__database.commit()
    def insertData(self,uid,username,password,gecos, homedir, shell, lastpasschange, minimum, maximum, warn, inactive, expire, gid,truncate=False):
        self.__cursor.execute("INSERT INTO user (`uid`,`username`,`password`, `lastpswdchange`, `minimum`, `maximum`, `warn`, `inactive`, `expire`, `shell`, `homedir`, `gecos`, `gid`) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}','{10}','{11}','{12}');".format(str(uid),str(username),str(password),str(lastpasschange), str(minimum), str(maximum), str(warn), str(inactive), str(expire),str(shell), str(homedir), str(gecos), str(gid)))
        self.__database.commit()
        """
        try:
            if truncate:
                self.__cursor.execute("TRUNCATE TABLE user;")
            self.__cursor.execute("INSERT INTO user (`uid`,`username`,`password`, `lastpswdchange`, `minimum`, `maximum`, `warn`, `inactive`, `expire`, `shell`, `homedir`, `gecos`, `gid`) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}','{10}','{11}','{12}');".format(str(uid),str(username),str(password),str(lastpasschange), str(minimum), str(maximum), str(warn), str(inactive), str(expire),str(shell), str(homedir), str(gecos), str(gid)))
            self.__database.commit()
        except:
            print('Error Inserting Data...')
            print('trying again...')
        """
#D = DatabaseEngine()
#D.createTables()
#D.insertData()
#D.visualizeDate()
