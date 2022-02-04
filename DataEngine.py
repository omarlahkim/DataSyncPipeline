import json
from DatabaseEngine import DatabaseEngine
from paramiko import client
import paramiko
#TODO
# Get Config from config.json file
# Connect to remote servers
# Get Files from remote servers

# Base Engine to manipulate data
class DataEngine(DatabaseEngine):
    def __init__(self):
        self.__config = json.load(open('config.json','r'))
        #self.__dbEngine=DatabaseEngine()
        self.__shadowClient = client.SSHClient()
        self.__passwdClient = client.SSHClient()
    # read data from csv
    def remoteconnection(self,client,remoteConfig):
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting to " + remoteConfig["Host"] + " ...")
        try:
            client.connect(remoteConfig["Host"], 22, remoteConfig["User"], remoteConfig["Pass"])
            print("Connected to " + remoteConfig["Host"] + " ...")
        except:
            print("Connection failed to "+remoteConfig["Host"]+" ")
            print("Trying again...")
            self.remoteconnection(client, remoteConfig)
    def init_connection(self):
        self.remoteconnection(self.getPasswdClient(), self.remotePasswdConfig())
        self.remoteconnection(self.getShadowClient(), self.remoteShadowConfig())
    def remoteShadowConfig(self):
        return self.__config['shadow']
    def remotePasswdConfig(self):
        return self.__config['passwd']
    def getPath(self,fileName):
        return self.__config[fileName]["Path"]
    def getFile(self, client, fileName):
        return client.open_sftp().open(self.getPath(fileName), 'r')
    def saveFile(self,client,fileName):
        open(fileName,'w').writelines(self.getFile(client,fileName).readlines())
    def getShadowClient(self):
        return self.__shadowClient
    def getPasswdClient(self):
        return self.__passwdClient
    def checkChange(self,client,fileName):
        try:
            oldData =  self.read(None,fileName)
            newData = self.read(client,fileName)
            if set(sum(oldData,[])) == set(sum(newData,[])):
                return False
        except:
            return True

    def read(self,client,fileName):
        if client != None:
            data=self.getFile(client,fileName)
        else:
            data= open(fileName,'r')
        data = data.readlines()
        for i in range(0,len(data)):
            data[i] = str(data[i].rstrip('\n')).split(':')
            for j in range(len(data[i])):
                if data[i][j] == '':
                    data[i][j] = "NULL"
                if data[i][j] == '*':
                    data[i][j] = "!"
        return data
    def checkFilesChange(self):
        if self.checkChange(self.getPasswdClient(),'passwd') == False and self.checkChange(self.getShadowClient(),'shadow') == False:
            return False
        else:
            return True
    # join passwd and shadow
    def join(self,passwdContent,shadowContent):
        if len (passwdContent)>= len (shadowContent):
            for i in range(0,len(shadowContent)):
                for j in range(0,len(passwdContent)):
                    if shadowContent[i][0] == passwdContent[j][0]:
                        passwdContent[j][1] = shadowContent[i][1]
                        for f in range(2,len(shadowContent[i])-1):
                            passwdContent[j].append(shadowContent[i][f].replace('\n',''))
        #newSchema = Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)
        return passwdContent
    #insert data into database
    def insert(self,data):
      pass
    # execute the pipeline
    def run(self):
        Passwd = self.read('passwd')
        Shadow = self.read('shadow')
        d.join(Passwd, Shadow)
        #self.insert(self.getDBConfig())

# Shadow: Username:Password:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)
# Passwd: Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell

# newSchema = Username:Password:User ID:Group ID (GID):User ID Info (GECOS):Home directory:Command/shell:Last password change:Minimum(days for pswd change):Maximum(days pswd validity):Warn(number of days before the user is warned about pswd expiration):Inactive:Expire(account expiration date)

