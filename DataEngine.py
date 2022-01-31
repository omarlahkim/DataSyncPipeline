import json
from DatabaseEngine import DatabaseEngine
# Base Engine to manipulate data
class DataEngine(DatabaseEngine):
    def __init__(self):
        pass
    # read data from csv
    def read(self,file):
        data=open(file,'r')
        data = data.readlines()
        for i in range(0,len(data)):
            data[i] = data[i].split(':')
        return data

    # join passwd and shadow
    def join(self,passwdContent,shadowContent):
        if len (passwdContent)>= len (shadowContent):
            for i in range(0,len(shadowContent)):
                for j in range(0,len(passwdContent)):
                    if shadowContent[i][0] == passwdContent[j][0]:
                        for f in range(2,len(shadowContent[i])-1):
                            passwdContent[j].append(shadowContent[i][f])
        # newSchema = Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)
        return passwdContent

    #insert data into database
    def insert(self,data,databaseConfig):
      pass
    # execute the pipeline
    def run(self):
        Passwd = self.read('passwd')
        Shadow = self.read('shadow')
        d.join(Passwd, Shadow)
        #self.insert(self.getDBConfig())

    def getDBConfig(self):
        return self.databaseConfig





# Shadow: Username:Password:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)
# Passwd: Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell

# newSchema = Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)


d = DataEngine()
#print(d.read('passwd'))
Passwd = d.read('passwd')
Shadow = d.read('shadow')
da = d.join(Passwd,Shadow)
data = da[1]
print(data)
db = DatabaseEngine()
db.insertData(data[2],data[0],data[1],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[3])
